def solve_hanoi(n_disks):
    if(n_disks == 0):
        return
    solve_hanoi(n_disks-1)
    move_disk(n_disks-1)
    solve_hanoi(n_disks-1)


def move_disks(n_disks):
    return -1