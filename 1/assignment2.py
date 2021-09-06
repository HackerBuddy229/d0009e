import Recipe
import BakingTimeCalculator
import BakingTimePresenter


def run(antal):
    mixing_time = BakingTimeCalculator.tid_blanda(antal)
    baking_time = BakingTimeCalculator.tid_grädda(antal)

    Recipe.recept(antal)
    BakingTimePresenter.present(mixing_time, baking_time)

    print("-------------")


run(4)
run(7)

