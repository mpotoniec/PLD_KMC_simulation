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
    #@profile
    def __init__(self, parameters) -> None:
        start_time = time.perf_counter()

        self.__parameters = parameters
        print('Parametry symulacji to: Rozmiar przestrzeni =', self.__parameters.space_size, 'Temperatura =', self.__parameters.substrate_temperature)
        self.__space = KMCmodel.space.Space(self.__parameters)
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
        #print('')
        self.__initTimeSec = finish_time - start_time

        self.print_memory_ussage('Użycie pamięci w funkcji init engine')
        print('Czas działania funkcji init (utworzenie przestrzeni do symulacji):', to_print_time_sec, '|', to_print_time_hmmssms)
     

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

    #@profile
    def startCalculations(self) -> int:
        start_time = time.perf_counter()






        #WYKONANIE SUMULACJI ZAPIS DO PLIKU ITP.
        #writerThread = threading.Thread(target=self.__writer) #Wykonanie zapisu do pliku w osobnym wątku.
        #writerThread.start() #Uruchomienie wątku do zapisu do pliku.

        #self.__makeCalculations() #Wykonanie obliczeń w głównym wątku.
        #writerThread.join() #Zakończenie działania wątku do zapisu do pliku.

        #self.__makeCalculations_writer_on_main_thread() #Wykonanie obliczeń oraz zapisu w głównym wątku.
        #WYKONANIE SUMULACJI ZAPIS DO PLIKU ITP.







        #MIERZENIE I PRZETWARZANIE CZASU DO WYPISANIA.
        finish_time = time.perf_counter()
        to_print_time_sec = str(round(finish_time - start_time, 2)) + '[s]'
        to_print_time_hmmssms = str(datetime.timedelta(seconds = finish_time - start_time)) + '[h:mm:ss:ms]'

        entire_time_sec = self.__initTimeSec + finish_time - start_time
        entire_time_hmmssms = str(datetime.timedelta(seconds = entire_time_sec)) + '[h:mm:ss:ms]'
        entire_time_sec = str(round(entire_time_sec, 2)) + '[s]'
        #MIERZENIE I PRZETWARZANIE CZASU DO WYPISANIA.






        #WYPISANIE STATYSTYK ZJAWISK WYSTĘPUJĄCYCH W SYMULACJI.
        print('')
        print('Ilość wystąpień adsorpcji:', self.__adsorptionCount, 'oraz dyfuzji', self.__diffusionCount, 'i None', self.__NoneCount)
        print('Ilość wystąpień wszystkich zdarzeń:', self.__adsorptionCount + self.__diffusionCount + self.__NoneCount)
        print('Possible Diffusions ilość:', len(self.__space.possibleDiffusions))
        print('Ilość zdarzeń adsorpcji: ', len(self.__space.adsorptionList))
        print('Ilość dodanych target dyfuzji do adsorptionList:', self.__diffusion_adsorption_add_targetCount)
        print('Ilość dodanych origin dyfuzji do adsorptionList:', self.__diffusion_adsorption_add_originCount)
        print('')
        #WYPISANIE STATYSTYK ZJAWISK WYSTĘPUJĄCYCH W SYMULACJI.







        #WYPISANIE CZASU WYKONANIA PROGRAMU.
        print('Czas trwania symulacji (bez twrozenia przestrzeni):', to_print_time_sec, '|', to_print_time_hmmssms)
        print('Czas wykonania całego programu:', entire_time_sec, '|', entire_time_hmmssms)
        #WYPISANIE CZASU WYKONANIA PROGRAMU.

        #self.print_memory_ussage('Użycie pamięci po zakończeniu działania programu')

        return 0

    def __cumulatedProbability(self) -> EventsProbability:
        adsorption_cumulated_probability = self.__parameters.adsorption_probability * len(self.__space.adsorptionList)
        diffusion_cumulated_probability = self.__space.cumulated_probability

        return self.EventsProbability(diffusion_cumulated_probability, adsorption_cumulated_probability)

    def __findEvent(self, events_probability: EventsProbability):

        rng_value = self.__rng.random()
        eventTypePointer = events_probability.all * rng_value
        
        if eventTypePointer <= events_probability.adsorption:
            return self.__space.adsorptionList[self.__rng.randint(0, len(self.__space.adsorptionList) - 1)]
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
                #print('Ilość zdarzeń adsorpcji: ', len(self.__space.adsorptionList))
                #print('Ilość dodanych target dyfuzji do adsorptionList:', self.__diffusion_adsorption_add_targetCount)
                #print('Ilość dodanych origin dyfuzji do adsorptionList:', self.__diffusion_adsorption_add_originCount)




        if isinstance(event, KMCmodel.adsorption.Adsorption): #ADSORPCJA
            self.__adsorptionCount+=1

            cell = event.cell

            if cell.y + 1 == self.__space.size.height:
                self.__isComplited = True
                return 0

            self.__space.cells_setColor(cell.x, cell.y, cell.z)

            adsEv = KMCmodel.adsorption.Adsorption(self.__space.cells[cell.x][cell.y + 1][cell.z], self.__parameters.adsorption_probability)
            self.__space.adsorptionList[self.__space.adsorptionList.index(event)] = adsEv





        elif isinstance(event, KMCmodel.diffusion.Diffusion): #DYFUZJA
            self.__diffusionCount+=1

            origin = event.originCell
            target = event.targetCell

            self.__space.cells_setColor(target.x, target.y, target.z)
            self.__space.cells_setTransparent(origin.x, origin.y, origin.z)

            #Change adsorption of target cell
            try:
                tmp_target_ads = KMCmodel.adsorption.Adsorption(target, self.__parameters.adsorption_probability) 
                adsEv_target_index = self.__space.adsorptionList.index(tmp_target_ads)

                del tmp_target_ads

            except ValueError: adsEv_target_index = None 

            if adsEv_target_index != None:
                self.__diffusion_adsorption_add_targetCount+=1
                baceCell_target = target
                
                if baceCell_target.y + 1 == self.__space.size.height:
                    self.__isComplited = True
                    return 0
                
                self.__space.adsorptionList[adsEv_target_index] = KMCmodel.adsorption.Adsorption(self.__space.cells[baceCell_target.x][baceCell_target.y + 1][baceCell_target.z], self.__parameters.adsorption_probability)

            #Change adsorption of origin cell
            try:
                tmp_cell = KMCmodel.cell.Cell(origin.x, origin.y + 1, origin.z, self.__parameters.energyAA)
                tmp_origin_ads = KMCmodel.adsorption.Adsorption(tmp_cell, self.__parameters.adsorption_probability) 
                adsEv_origin_index = self.__space.adsorptionList.index(tmp_origin_ads)
                
                del tmp_origin_ads
                del tmp_cell

            except ValueError: adsEv_origin_index = None         
                
            if adsEv_origin_index != None:
                self.__diffusion_adsorption_add_originCount+=1
                baceCell_origin = origin
 
                self.__space.adsorptionList[adsEv_origin_index] = KMCmodel.adsorption.Adsorption(self.__space.cells[baceCell_origin.x][baceCell_origin.y][baceCell_origin.z], self.__parameters.adsorption_probability)
            



        else:
            self.__NoneCount+=1 
            print('None przeszło')
            return - 1            

        return 0



    def __makeCalculations(self) -> None:

        while(not self.__isComplited):

            propabilitySums = self.__cumulatedProbability()
            self.__handleEvent(self.__findEvent(propabilitySums))

            self.__time += 1 / propabilitySums.all
            
            #self.printads()
            #self.printstate()
        #self.printstate()

    def __makeCalculations_writer_on_main_thread(self) -> None:

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
        times = []

        while(not self.__isComplited):

            propabilitySums = self.__cumulatedProbability()
            self.__handleEvent(self.__findEvent(propabilitySums))

            self.__time += 1 / propabilitySums.all

            if timePointer >= self.__time:
                continue
            else:
                timePointer += 10
                start_time = time.perf_counter()
                self.__writer_for_main_thread(file)
                stop_time = time.perf_counter()
                times.append(stop_time - start_time)            
        
        file.close()

        avarage_sec = sum(times)/len(times)
        avarage_hmmssms = str(datetime.timedelta(seconds = avarage_sec)) + '[h:mm:ss:ms]'
        avarage_sec = str(round(avarage_sec, 2)) + '[s]'

        print('Liczba zapisów =', len(times), 'Sredni czas zapisu =', avarage_sec, '|', avarage_hmmssms)



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

        times = []
        while self.__isComplited == False:

            if timePointer >= self.__time:
                time.sleep(0.05)
                continue
            
            timePointer += 10

            start_time = time.perf_counter()
            
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
                        
                        color = self.__space.cells_getColor(cell.x, cell.y, cell.z)

                        file.write(str(id(cell))       + " " +
                        str(cell.x + 0.5)              + " " +
                        str(cell.z + 0.5)              + " " +
                        str(cell.y + 0.5)              + " " +
                        str(color.R / 255.0)           + " " +
                        str(color.G / 255.0)           + " " +
                        str(color.B / 255.0)           + " " +
                        str(int(1 - color.A / 255))    + " " +
                        str(id(color))                 + "\n")

            stop_time = time.perf_counter()
            times.append(stop_time - start_time)

        file.close()
        
        avarage_sec = sum(times)/len(times)
        avarage_hmmssms = str(datetime.timedelta(seconds = avarage_sec)) + '[h:mm:ss:ms]'
        avarage_sec = str(round(avarage_sec, 2)) + '[s]'


        print('Liczba zapisów =', len(times), 'Sredni czas zapisu =', avarage_sec, '|', avarage_hmmssms)
        
    def __writer_for_main_thread(self, file) -> None:
            
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
                
                    color = self.__space.cells_getColor(cell.x, cell.y, cell.z)

                    file.write(str(id(cell))       + " " +
                    str(cell.x + 0.5)              + " " +
                    str(cell.z + 0.5)              + " " +
                    str(cell.y + 0.5)              + " " +
                    str(color.R / 255.0)           + " " +
                    str(color.G / 255.0)           + " " +
                    str(color.B / 255.0)           + " " +
                    str(int(1 - color.A / 255))    + " " +
                    str(id(color))                 + "\n")



    def printstate(self):
        print('Tablica komórek')
        for cell_tab1 in self.__space.cells:
            for cell_tab2 in cell_tab1:
                for cell in cell_tab2:
                    print(cell)

    def printads(self):
        print('Tablica wszystkich adsorpcji')
        for adsorption in self.__space.adsorptionList:
            print(adsorption)

    def print_memory_ussage(self, info = 'Użycie pamięci'):
        print('')
        print(info)
        import os, psutil

        MB = 1048576
        GB = 1073741824

        process = psutil.Process(os.getpid())

        resident_memory = process.memory_info()[0]
        virtual_memory = process.memory_info()[1]
        shared_memory = process.memory_info()[2]
        data_memory = process.memory_info()[5]

        print(f'Pamięć rezydenta       = {round(resident_memory / MB, 2)}[MB] | {round(resident_memory / GB, 2)}[GB]')
        print(f'Pamięć wirtualna       = {round(virtual_memory / MB, 2)}[MB] | {round(virtual_memory / GB, 2)}[GB]')
        print(f'Pamięć współdzielona   = {round(shared_memory / MB, 2)}[MB] | {round(shared_memory  / GB, 2)}[GB]')
        print(f'Pamięć danych (RAM)    = {round(data_memory / MB, 2)}[MB] | {round(data_memory / GB, 2)}[GB]')
        print('')