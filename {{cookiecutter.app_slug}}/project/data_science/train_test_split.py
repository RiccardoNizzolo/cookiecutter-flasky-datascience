from sklearn.model_selection import train_test_split as tts


def train_test_split_simple(x,y):
    return tts(x, y, test_size = 0.33,shuffle=False )

def train_test_split_random(x,y):
    return tts(x, y, test_size = 0.33,shuffle=False )