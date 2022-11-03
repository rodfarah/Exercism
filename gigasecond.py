from datetime import timedelta


def add(moment):
    ''' Given a moment, determine the moment that would be after a gigasecond (10**9 seconds) has passed'''

    gs = timedelta(seconds=10**9)

    return moment + gs

