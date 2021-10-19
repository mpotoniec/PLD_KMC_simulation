import KMCmodel.parameters
import KMCmodel.size3D
import KMCmodel.space
import KMCmodel.cell
import KMCmodel.adsorption
import KMCmodel.diffusion

import threading
import datetime
import platform
import random

import time

class Engine():
    def __init__(self) -> None:
        start_time = time.perf_counter()

        self.__parameters = KMCmodel.parameters.Parameters()
        print('Parametry symulacji to: Rozmiar przestrzeni =', self.__parameters.space_size, 'Temperatura =', self.__parameters.substrate_temperature)
        self.__space = KMCmodel.space.Space(KMCmodel.size3D.Size3D(self.__parameters.space_size, self.__parameters.space_size, self.__parameters.space_size))
        self.__adsorptionList = [None for _ in range(self.__space.size.width * self.__space.size.depth)]
        self.__rng = random

        self.__isComplited = False
        self.__time = 0

        self.__step = 0
        self.__adsorptionCount = 0
        self.__diffusionCount = 0
        self.__NoneCount = 0

        self.__diffusion_adsorption_add_targetCount = 0
        self.__diffusion_adsorption_add_originCount = 0

        finish_time = time.perf_counter()
        to_print_time_sec = str(round(finish_time - start_time, 2)) + '[s]'
        to_print_time_hmmssms = str(datetime.timedelta(seconds = finish_time - start_time)) + '[h:mm:ss:ms]'
        print('Czas działania funkcji init (utworzenie przestrzeni do symulacji):', to_print_time_sec, '|', to_print_time_hmmssms)

        self.__initTimeSec = finish_time - start_time
     

    class EventsProbability():
        def __init__(self, diffusion, adsorption) -> None:
            self.__diffusion = diffusion
            self.__adsorption = adsorption
            self.__all = self.__diffusion + self.__adsorption

        @property
        def diffusion(self):
            return self.__diffusion
        @diffusion.setter
        def diffusion(self, diffusion):
            self.__diffusion = diffusion
            self.__all = self.__diffusion + self.__adsorption
        @property
        def adsorption(self):
            return self.__adsorption
        @adsorption.setter
        def adsorption(self, adsorption):
            self.__adsorption = adsorption
            self.__all = self.__diffusion + self.__adsorption
        @property
        def all(self):
            return self.__all
        
        def __str__(self) -> str:
            return ('Prawdopodobieństwo adsorpcji: '+ str(self.__adsorption)
            + '. Prawdopodobieństwo dyfuzji: ' + str(self.__diffusion)
            + '. Prawdopodobieństwo całkowite (ALL): ' + str(self.__all))

    def startCalculations(self) -> int:
        start_time = time.perf_counter()

        calculationsThread = threading.Thread(target=self.__makeCalculations)
        writerThread = threading.Thread(target=self.__writer)

        calculationsThread.start()
        writerThread.start()
        calculationsThread.join()
        writerThread.join()
        
        finish_time = time.perf_counter()
        to_print_time_sec = str(round(finish_time - start_time, 2)) + '[s]'
        to_print_time_hmmssms = str(datetime.timedelta(seconds = finish_time - start_time)) + '[h:mm:ss:ms]'
        print('Czas trwania symulacji (bez twrozenia przestrzeni):', to_print_time_sec, '|', to_print_time_hmmssms)

        entire_time_sec = self.__initTimeSec + finish_time - start_time
        entire_time_hmmssms = str(datetime.timedelta(seconds = entire_time_sec)) + '[h:mm:ss:ms]'
        entire_time_sec = str(round(entire_time_sec, 2)) + '[s]'
        print('Czas wykonania całego programu:', entire_time_sec, '|', entire_time_hmmssms)

        return 0



    def __prepareCalculations(self) -> int:

        self.__initEvents()
        return 0

    def __initEvents(self) -> None:

        index = 0
        for i in range(self.__space.size.width):
            for k in range(self.__space.size.depth):
                self.__createAdsorptionForCell(self.__space.cells[i][0][k], index)
                index+=1

    def __createAdsorptionForCell(self, cell: KMCmodel.cell.Cell, index: int) -> None:
        self.__adsorptionList[index] = KMCmodel.adsorption.Adsorption(cell, self.__parameters.adsorption_probability)

    def __cumulatedProbability(self) -> EventsProbability:
        adsorption_cumulated_probability = self.__parameters.adsorption_probability * len(self.__adsorptionList)
        diffusion_cumulated_probability = self.__space.cumulated_probability

        return self.EventsProbability(diffusion_cumulated_probability, adsorption_cumulated_probability)

    def __findEvent(self, events_probability: EventsProbability):

        rng_value = self.__rng.random()
        eventTypePointer = events_probability.all * rng_value
        
        if eventTypePointer <= events_probability.adsorption:
            return self.__adsorptionList[self.__rng.randint(0, len(self.__adsorptionList) - 1)]
        else:
            diffusionPointer = events_probability.diffusion * self.__rng.random()
            diffusion_probability_sum = 0.

            for diffusion in self.__space.possibleDiffusions:
                diffusion_probability_sum += diffusion.probability
                if diffusion_probability_sum >= diffusionPointer: return diffusion

            return None

    def __handleEvent(self, event):
        #print('Wybrane zdarzenie to:', event)

        if isinstance(event, KMCmodel.adsorption.Adsorption):
            if event.cell.y + 1 > self.__step:
                self.__step = event.cell.y + 1
                pr_value = (self.__step * 100) / self.__space.size.height
                pr_value = round(pr_value, 1)
                to_print_value = str(pr_value) + '%'
                print('Symulacja ukończona w:', to_print_value)
                #print('Ilość wystąpień adsorpcji:', self.__adsorptionCount, 'oraz dyfuzji', self.__diffusionCount, 'i None', self.__NoneCount)
                #print('Ilość wystąpień wszystkich zdarzeń:', self.__adsorptionCount + self.__diffusionCount + self.__NoneCount)
                #print('Possible Diffusions ilość:', len(self.__space.possibleDiffusions))
                #print('Ilość zdarzeń adsorpcji: ', len(self.__adsorptionList))
                #print('Ilość dodanych target dyfuzji do adsorptionList:', self.__diffusion_adsorption_add_targetCount)
                #print('Ilość dodanych origin dyfuzji do adsorptionList:', self.__diffusion_adsorption_add_originCount)

        if isinstance(event, KMCmodel.adsorption.Adsorption): #ADSORPCJA
            self.__adsorptionCount+=1

            cell = event.cell

            if cell.y + 1 == self.__space.size.height:
                self.__isComplited = True
                return 0

            cell.color = cell.getMostPopularColorInNeighbourhood()
            if cell.color.A == 0:
                cell.color = self.__space.getColorAtIndex(self.__space.getNewColor())
            self.__space.cells_setColor(cell.x, cell.y, cell.z, cell.color)

            adsEv = KMCmodel.adsorption.Adsorption(self.__space.cells[cell.x][cell.y + 1][cell.z], self.__parameters.adsorption_probability)
            #self.__adsorptionList[self.__adsorptionList == event] = adsEv
            #event = adsEv
            self.__adsorptionList[self.__adsorptionList.index(event)] = adsEv





        elif isinstance(event, KMCmodel.diffusion.Diffusion): #DYFUZJA
            self.__diffusionCount+=1

            origin = event.originCell
            target = event.targetCell


            target.color = target.getMostPopularColorInNeighbourhood()
            if target.color.A == 0:
                target.color = self.__space.getColorAtIndex(self.__space.getNewColor())
            self.__space.cells_setColor(target.x, target.y, target.z, target.color)
            
            origin.color = self.__space.getColorAtIndex(0)
            self.__space.cells_setColor(origin.x, origin.y, origin.z, origin.color)

            #Change adsorption of target cell
            #adsEv_target_index = None
            #for i in range(len(self.__adsorptionList)):
            #    if self.__adsorptionList[i].cell == target:
            #        adsEv_target_index = i
            #        break

            try:
                tmp_target_ads = KMCmodel.adsorption.Adsorption(target, self.__parameters.adsorption_probability) 
                adsEv_target_index = self.__adsorptionList.index(tmp_target_ads)

                del tmp_target_ads

            except ValueError: adsEv_target_index = None 

            if adsEv_target_index != None:
                self.__diffusion_adsorption_add_targetCount+=1
                baceCell_target = target
                
                if baceCell_target.y + 1 == self.__space.size.height:
                    self.__isComplited = True
                    return 0
                
                self.__adsorptionList[adsEv_target_index] = KMCmodel.adsorption.Adsorption(self.__space.cells[baceCell_target.x][baceCell_target.y + 1][baceCell_target.z], self.__parameters.adsorption_probability)

            #Change adsorption of origin cell
            #adsEv_origin_index = None
            #for j in range(len(self.__adsorptionList)):
            #    if self.__adsorptionList[j].cell.x == origin.x and self.__adsorptionList[j].cell.y == origin.y + 1 and self.__adsorptionList[j].cell.z == origin.z:
            #        adsEv_origin_index = j
            #        break

            try:
                tmp_cell = KMCmodel.cell.Cell(origin.x, origin.y + 1, origin.z)
                tmp_origin_ads = KMCmodel.adsorption.Adsorption(tmp_cell, self.__parameters.adsorption_probability) 
                adsEv_origin_index = self.__adsorptionList.index(tmp_origin_ads)
                
                del tmp_origin_ads
                del tmp_cell

            except ValueError: adsEv_origin_index = None         
                
            if adsEv_origin_index != None:
                self.__diffusion_adsorption_add_originCount+=1
                baceCell_origin = origin
 
                self.__adsorptionList[adsEv_origin_index] = KMCmodel.adsorption.Adsorption(self.__space.cells[baceCell_origin.x][baceCell_origin.y][baceCell_origin.z], self.__parameters.adsorption_probability)
            



        else:
            self.__NoneCount+=1 
            print('None przeszło')
            return - 1            

        return 0

    def __makeCalculations(self) -> None:

        self.__prepareCalculations()

        while(not self.__isComplited):

            propabilitySums = self.__cumulatedProbability()
            self.__handleEvent(self.__findEvent(propabilitySums))

            self.__time += 1 / propabilitySums.all
            
            #self.printads()
            #self.printstate()
        #self.printstate()

    def __writer(self) -> None:
        if platform.system() == 'Linux':
            name = 'Results/output'+ str(datetime.datetime.now()).split('.')[0] + '.dump'

        elif platform.system() == 'Windows':
            name = 'Results/output'+ str(datetime.datetime.now()).split('.')[0] + '.dump'
            name_tab = name.split(':')
            name = ''
            for char in name_tab:
                name += char
  
        file = open(name, 'w')

        timePointer = 0

        while self.__isComplited == False:

            if timePointer >= self.__time:
                time.sleep(0.05)
                continue
            
            timePointer += 10

            file.write("ITEM: TIMESTEP\n")
            file.write(str(self.__time)+'\n')
            file.write("ITEM: NUMBER OF ATOMS\n")
            file.write(str(self.__space.size.volume_size)+'\n')
            file.write("ITEM: BOX BOUNDS pp pp pp\n")
            file.write("0 " + str(self.__space.size.width)+'\n')
            file.write("0 " + str(self.__space.size.height)+'\n')
            file.write("0 " + str(self.__space.size.depth)+'\n')
            file.write("ITEM: ATOMS id x y z R G B A column_id\n")

            for cell_tab in self.__space.cells:
                for cell_tab2 in cell_tab:
                    for cell in cell_tab2:
                
                        file.write(str(id(cell))       + " " +
                        str(cell.x + 0.5)              + " " +
                        str(cell.z + 0.5)              + " " +
                        str(cell.y + 0.5)              + " " +
                        str(cell.color.R / 255.0)      + " " +
                        str(cell.color.G / 255.0)      + " " +
                        str(cell.color.B / 255.0)      + " " +
                        str(1 - cell.color.A / 255)    + " " +
                        str(id(cell.color))            + "\n")

        file.close()




    def printstate(self):
        print('Tablica komórek')
        for cell_tab1 in self.__space.cells:
            for cell_tab2 in cell_tab1:
                for cell in cell_tab2:
                    print(cell)

    def printads(self):
        print('Tablica wszystkich adsorpcji')
        for adsorption in self.__adsorptionList:
            print(adsorption)