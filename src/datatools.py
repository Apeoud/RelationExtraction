"""
这个文件主要用来读取读取数据，然后转成格式统一的数据形式。

"""


# 参考tensorflow等example中是如何处理数据结构的
class REDataset:
    """
    数据集类，每个数据集都是多个句子(实例)的集合，每个实例对应有ID和label。
    """

    def __init__(self):
        self.name = ""
        self.instances = list()

        self.labels = list()

        self.number_sentences = 0


class RESentence:
    """
    句子类，每个句子都包含一个mention，两个实体，两个实体对应的位置
    """

    def __init__(self, mention, e1_mention, e2_mention, e1_pos, e2_pos, e1_id, e2_id, ):
        self.mention = mention

        # optional
        self.e1_id = e1_id
        self.e2_id = e2_id

        self.e1_mention = e1_mention
        self.e2_mention = e2_mention

        self.e1_pos = e1_pos
        self.e2_pos = e2_pos


if __name__ == "__main__":
    print("end")
