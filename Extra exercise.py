"""Extra exercise.py"""


people_list = [["Vaike Marek", "Softball", "Gaming"], ["Eerik Eero", "Winemaking", "Car fixing & building", "Something"], ["Eve Kaidi", "Decorating", "Hydroponics",], ["Siiri Kersti", "Digital hoarding", "Sledding"], ["Ene Rutt", "Barbershop Music", "Drama"]]


def filter_by_hobby(people_list: list, hobby: str) -> list:
    """
    Return list of people that have the given hobby in their list of hobbies.

    :param people_list: input list of people.
    :param hobby: hobby to filter by.
    :return: filtered list of people.
    """
    for person in people_list:
        if hobby in person:
            return person


def sort_by_most_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in descending order.

    Highest amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    people_list.sort(key=len, reverse=True)
    return people_list


def sort_by_least_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in ascending order.

    Least amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    people_list.sort(key=len)
    return people_list


def sort_people_and_hobbies(people_list: list) -> list:
    """
    Return a list of people but sorted alphabetically by their full name.
    Also sort their list of hobbies alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    people_list = sorted(people_list, key=lambda x: x[0])
    return people_list

print(sort_by_most_hobbies(people_list))
print(sort_by_least_hobbies(people_list))
print(sort_people_and_hobbies(people_list))