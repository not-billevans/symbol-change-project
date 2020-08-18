import pandas as pd
import time
start_time = time.time()

# Suffix added to a_sym1. (GOOG -> GOOG_A)
suf1 = '_A'
# Suffix added to a_sym2 (GOOGL -> GOOGL_1)
suf2 = '_1'


def change_symbol(a_sym1, a_sym2):
    # Function change_symbol takes two string inputs, a_sym1 and a_sym2, each a stock symbol. In 'in_file.csv':
    # 1) a_sym1, a_sym1 -> a_sym1, a_sym2 + suf1, suf2; 2) first letter of symbol; 3) last letter of
    # symbol; 4) contents of #1.

    # Changed symbols
    a = 0
    # First letter
    b = 1
    # Last letter
    c = 2
    # Changed symbols
    d = 3

    # Each function refers to the original input file at index 0. The above variables store
    # the ZERO-INDEXED COLUMN NUMBERS for each of the below functions' outputs.  E.g.,
    # if a = 1, the first function will output to the 2nd column of the output file.

    # IMPORTANT: EACH VALUE MUST BE DISTINCT FROM THE OTHERS. NO TWO VARIABLES CAN HAVE THE
    # SAME VALUE ASSIGNED TO THEM. OUTPUT WILL BE OVERWRITTEN!

    df_in = pd.read_csv('in_file.csv', delimiter='\t', header=None, index_col=False)
    print(df_in.describe)
    # Changed symbols
    df_in[a] = df_in[0].replace((a_sym1, a_sym2), (a_sym1 + suf1, a_sym2 + suf2))
    # First letter
    df_in[b] = df_in[0].str[:1]
    # Last letter
    df_in[c] = df_in[0].str[-1:]
    # Changed symbols
    df_in[d] = df_in[0]

    # Save to output file, excluding headers and index labels.
    df_in.to_csv('out_file.csv', header=None, index=False)
    # print(df_in)
    print("--- %s seconds ---" % (time.time() - start_time))


# This block executes function change_symbol:
change_symbol('GOOG', 'GOOGL')


def change_symbol_back(b_sym1, b_sym2):
    # Function change_symbols_back takes two string inputs - EQUAL TO THE OUTPUTS OF change_symbol !!! - and
    # reverts them back to their original form IN THE FOURTH COLUMN, ONLY! In other words, if 'GOOG'
    # became 'GOOG_A', this function will output 'GOOG' in the fourth column of the output file.

    a = 3

    a_sym1 = b_sym1[:-len(suf1)]
    a_sym2 = b_sym2[:-len(suf2)]

    df_out = pd.read_csv('out_file.csv', header=None)
    print(df_out.describe)
    df_out[a] = df_out[a].replace((b_sym1, b_sym2), (a_sym1, a_sym2))

    # Save to output file, excluding headers and index labels.
    df_out.to_csv('out_file.csv', header=None, index=False)
    # print(df_out)
    print("--- %s seconds ---" % (time.time() - start_time))

# This block executes change_symbol_back:


change_symbol_back('GOOG_A', 'GOOGL_1')

