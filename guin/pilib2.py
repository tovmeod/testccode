from pi3._pi import lib


def pi_approx(n: int) -> float:
    return lib.pi_approx(n)
# $env:PYNGUIN_DANGER_AWARE=1
# PYNGUIN_DANGER_AWARE=1 pynguin --project-path . --output-path guin/testpi --module-name guin.pilib2
