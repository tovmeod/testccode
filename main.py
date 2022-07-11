from pi._pi import lib


def run_approx():
    approx = lib.pi_approx(10)
    assert str(approx).startswith("3.")

    approx = lib.pi_approx(10000)
    assert str(approx).startswith("3.1")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # run_approx()
    approx = lib.pi_approx(1)
    assert str(approx).startswith("3.")
