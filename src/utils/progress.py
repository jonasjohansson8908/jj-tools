"""
    progress.py is a scalable loading bar that uses carriage return to print and
    update the progress on stdout. The percentage of the progress is also shown.

    Author: Jonas Johansson, jonasjo5@kth.se
"""

import time

def update_progress(progress, msg_pre='', msg_post='', scaling=1):
    """Formats and prints the progress as a progress bar to stdout.

    Args:
        progress (int): The progress that is to be printed. Given as an integer value
                        between 0-100 which corresponds to the progress percentage.
        msg_pre (str), optional: Message that if provided, will be shown before the
                                 progress bar.
    """
    # limit the progress to 0-100% and round to integer number
    if progress > 100:
        progress = 100
    elif progress < 0:
        progress = 0
    else:
        progress = round(progress)

    # force scaling to integer value
    if scaling < 1:
        scaling = 1
    else:
        scaling = round(scaling)

    # calculate filled and empty elements
    n_filled = (scaling * progress // 10)
    n_empty = scaling * 10 - n_filled

    # print the progress bar
    print('\r{0} [{1}] {2}% {3}'.format(msg_pre, '#' * n_filled + '-' * n_empty,
                                        progress, msg_post), end='')

def main():
    """ Main method to run an example of the progress bar.
    """
    for progress in range(0, 110, 5):
        update_progress(progress, scaling=3, msg_pre="installing software:", msg_post="done")
        time.sleep(0.3)
    print("\nInstallation complete!")


if __name__ == "__main__":
    main()
