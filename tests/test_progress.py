"""
Tests for the functions of utils/progress.py
"""

from src.utils.progress import update_progress

def test_progress_bar(capsys):
    """
    Tests of the function progress_bar()
    """
    # test empty progress bar
    update_progress(0)
    captured = capsys.readouterr()
    assert captured.out == ('\r [----------] 0% ')

    # test negative input
    update_progress(-2)
    captured = capsys.readouterr()
    assert captured.out == ('\r [----------] 0% ')

    # test no progress with pre message
    update_progress(0, msg_pre='installing')
    captured = capsys.readouterr()
    assert captured.out == ('\rinstalling [----------] 0% ')

    # test no progress with post message
    update_progress(0, msg_post='done')
    captured = capsys.readouterr()
    assert captured.out == ('\r [----------] 0% done')

    # test no progress with pre and post message
    update_progress(0, msg_pre='installing', msg_post='done')
    captured = capsys.readouterr()
    assert captured.out == ('\rinstalling [----------] 0% done')

    # test float input
    update_progress(79.9)
    captured = capsys.readouterr()
    assert captured.out == ('\r [########--] 80% ')

    # test too large input
    update_progress(150)
    captured = capsys.readouterr()
    assert captured.out == ('\r [##########] 100% ')

    # test scaled progress bar
    update_progress(70, scaling=2)
    captured = capsys.readouterr()
    assert captured.out == ('\r [##############------] 70% ')
    
    # test progress bar scaled with float
    update_progress(70, scaling=2.6)
    captured = capsys.readouterr()
    assert captured.out == ('\r [#####################---------] 70% ')
