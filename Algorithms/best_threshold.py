import argparse


ground_truths = {
    "AA56D_set6": [35438, 45679, 56132, 76437, 92538, 112236],
    "AA56D_set5": [38339,  52386,  80472,  93949, 110389, 127213],
    "AC17D_set5": [24574,  44832,  65498,  75827,  85830, 105950],
    "AC17D_set6": [32985,  42838,  59319,  85930,  99094, 115967],
    "AJ05D_set5": [29859,  44867,  59376,  73436,  94344, 111985],
    "AJ05D_set6": [34472,  46150,  57921,  98744, 111208, 130666],
    "AQ59D_set6": [30989,  45383,  80984,  94935, 105786, 116483],
    "AQ59D_set7": [20550,  32360,  51188,  62390,  73316, 119470],
    "AW59D_set6": [80025,  89766,  99353, 115699, 126243, 151322],
    "AW59D_set5": [28346,  53529,  72696,  82370,  94985, 104723],
    "AY63D_set5": [30827,  44573,  58691,  76108, 104608, 116030],
    "AY63D_set6": [33830,  48181,  68574,  88862, 106121, 123453],
    "BS34D_set6": [39528,  56616,  66819,  83440,  93522, 113575],
    "BS34D_set5": [29753,  39928,  50250,  83927,  94285, 110885],
    "BY74D_set5": [35875,  45760,  55458,  71575,  84799, 107807],
    "BY74D_set6": [63161,  79681,  99674, 116457, 126649, 143375]
}


def main(args):
    return 0.114514


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='find best threshold')
    main(parser.parse_args())
