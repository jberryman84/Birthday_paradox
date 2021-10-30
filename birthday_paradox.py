"""Birthday Paradox Simulation, by Al Sweigart



"""

import datetime, random
from typing import BinaryIO


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year of birthday is unimportant for our simulation
        # as long as the birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a randon day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthday list"""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique so return nothing

    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b in birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday

