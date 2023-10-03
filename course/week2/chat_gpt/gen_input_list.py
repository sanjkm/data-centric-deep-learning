import pandas as pd

INPUT_FILE = 'input_files/prompt_list.csv'
POST_FIELD, TOPIC_FIELD = 'post', 'topic'

if __name__ == '__main__':

    df = pd.read_csv(INPUT_FILE)

    post_list = df[POST_FIELD].tolist()

    for post_ex in post_list:
        print ("- ", post_ex)