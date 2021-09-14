import KMCmodel.parameters
import KMCmodel.size3D
import KMCmodel.space
import KMCmodel.cell
import KMCmodel.adsorption
import KMCmodel.diffusion

import numpy as np

import time as t

class Engine():
    '''adssd'''
    def __init__(self) -> None:
        start_time = t.perf_counter()

        self.__parameters = KMCmodel.parameters.Parameters()
        self.__space = KMCmodel.space.Space(KMCmodel.size3D.Size3D(self.__parameters.space_size, self.__parameters.space_size, self.__parameters.space_size))
        self.__adsorptionList = np.empty((self.__space.size.width * self.__space.size.depth),dtype=KMCmodel.adsorption.Adsorption,order='C')
        self.__rng = np.random

        self.__isComplited = False
        self.__step = 0
        self.__adsorptionCount = 0
        self.__diffusionCount = 0
        self.__NoneCount = 0

        finish_time = t.perf_counter()
        print(f'Czas działania funkcji init: {round(finish_time - start_time, 2)}[s] ')
     

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
        start_time = t.perf_counter()


        self.__prepareCalculations()

        time = 0

        print('WYKONANIE PROGRAMU')

        while(not self.__isComplited):

            propabilitySums = self.__cumulatedProbability()
            self.__handleEvent(self.__findEvent(propabilitySums))
            #self.__handleEvent(None)
            #self.__handleEvent(KMCmodel.diffusion.Diffusion(KMCmodel.cell.Cell(0,0,0), KMCmodel.cell.Cell(1,1,1)))

            time += 1 / propabilitySums.all

            #self.__isComplited = True
            #self.printstate()
        #self.printstate()
        print(f'Ilość wystąpień adsorpcji: {self.__adsorptionCount:,} oraz dyfuzji {self.__diffusionCount:,} i None {self.__NoneCount:,}')
        
        finish_time = t.perf_counter()
        print(f'Zakończenie działania programu w: {round(finish_time - start_time, 2)}[s] ')

        return 0



    def __prepareCalculations(self) -> int:

        self.__initEvents()
        return 0

    def __initEvents(self) -> None:

        index = 0
        for i in range(self.__space.size.width):
            for k in range(self.__space.size.depth):
                self.__createAdsorptionForCell(self.__space.cells[i, 0, k], index)
                index+=1

    def __createAdsorptionForCell(self, cell: KMCmodel.cell.Cell, index: int) -> None:
        self.__adsorptionList[index] = KMCmodel.adsorption.Adsorption(cell, self.__parameters.adsorption_probability)

    def __cumulatedProbability(self) -> EventsProbability:
        adsorption_cumulated_probability = self.__parameters.adsorption_probability * self.__adsorptionList.shape[0]
        diffusion_cumulated_probability = self.__space.cumulated_probability

        cumulated_probability = adsorption_cumulated_probability + diffusion_cumulated_probability

        return self.EventsProbability(diffusion_cumulated_probability, adsorption_cumulated_probability)

    def __findEvent(self, events_probability: EventsProbability):

        print('Ilość możliwych dyfuzji', len(self.__space.possibleDiffusions))
        print(events_probability)

        rng_value = self.__rng.random_sample()
        eventTypePointer = events_probability.all * rng_value
        
        if eventTypePointer <= events_probability.adsorption:
            return self.__adsorptionList[self.__rng.randint(0, self.__adsorptionList.shape[0])]
        else:
            diffusionPointer = events_probability.diffusion * self.__rng.random_sample()
            diffusion_probability_sum = 0.

            for diffusion in self.__space.possibleDiffusions:
                diffusion_probability_sum += diffusion.probability
                print(diffusion_probability_sum)
                if diffusion_probability_sum >= diffusionPointer: return diffusion

            return None

    def __handleEvent(self, event):
        #print(event)

        if isinstance(event, KMCmodel.adsorption.Adsorption): #ADSORPCJA
            #print('Adsorpcja przeszło')
            self.__adsorptionCount+=1

            cell = event.cell
            
            if cell.y + 1 > self.__step:
                self.__step = cell.y + 1
                pr_value = (self.__step * 100) / self.__space.size.height
                print(f'Symulacja ukończona w: {pr_value}%')



            if cell.y + 1 == self.__space.size.height:
                self.__isComplited = True
                return 0
            
            cell.color = cell.getMostPopularColorInNeighbourhood()
            if cell.color.A == 0:
                cell.color = self.__space.getColorAtIndex(self.__space.getNewColor())
            #print(cell.color)

            self.__space.cells_setColor(cell.x, cell.y, cell.z, cell.color)

            adsEv = KMCmodel.adsorption.Adsorption(self.__space.cells[cell.x, cell.y + 1, cell.z], self.__parameters.adsorption_probability)
            self.__adsorptionList[self.__adsorptionList == event] = adsEv
            #event.cell = self.__space.cells[cell.x, cell.y + 1, cell.z]

        elif isinstance(event, KMCmodel.diffusion.Diffusion): #DYFUZJA
            #print('Dufizja przeszło')
            self.__diffusionCount+=1

            origin = event.originCell
            target = event.targetCell

            target.color = target.getMostPopularColorInNeighbourhood()
            if target.color.A == 0:
                target.color = self.__space.getColorAtIndex(self.__space.getNewColor())
            origin.color = self.__space.getColorAtIndex(0)


        else:
            self.__NoneCount+=1 
            #print('None przeszło')
            return - 1            

        return 0


    def printstate(self):
        print('Tablica komórek')
        for cell_tab1 in self.__space.cells:
            for cell_tab2 in cell_tab1:
                for cell in cell_tab2:
                    print(cell)