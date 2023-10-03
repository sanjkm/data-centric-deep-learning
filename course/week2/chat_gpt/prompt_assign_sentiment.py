import pandas as pd

TRAINING_FILE = 'input_files/prompt_list.csv'
ASSIGN_FILE = 'input_files/ninety_chatgpt_sentences.csv'

POST_FIELD = 'post'
TOPIC_FIELD = 'topic'

if __name__ == '__main__':

    train_df = pd.read_csv(TRAINING_FILE)

    post_list, topic_list = train_df[POST_FIELD].tolist(), train_df[TOPIC_FIELD].tolist()

    for i in range(len(post_list)):

        print ("Example")
        print ("Input: ", post_list[i])
        print ("Output: ", topic_list[i])

    assign_df = pd.read_csv(ASSIGN_FILE, delimiter='\t')

    assigned_post_list = assign_df[POST_FIELD].tolist()

    for i in range(len(assigned_post_list)):

        print ("Task")
        print ("Input: ", assigned_post_list[i])
        print ("Output: ")
