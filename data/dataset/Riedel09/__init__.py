"""
dataset transformer function
"""

import codecs

from src.datatools import REDataset, RESentence


class RiedelDataset(REDataset):

    def __init__(self, fp):
        super().__init__()
        # todo:verify parameter
        self.ht_index = dict()

        self.parser(fp)
        return

    def parser(self, fp):
        """

        :param fp:
        :return:
        """

        self.instances = dict()
        self.labels = dict()

        for i, line in enumerate(codecs.open(fp, "r", encoding="UTF-8").readlines()):
            flag, s, label = self._parse_sentence(line)

            if flag:
                self.instances[i] = s
                self.labels[i] = label
                self.number_sentences += 1

                key = "%s\t%s" % (s.e1_id, s.e2_id)
                if key in self.ht_index.keys():
                    self.ht_index[key].append(i)
                else:
                    self.ht_index[key] = [i]
        return

    @staticmethod
    def _parse_sentence(sentence):
        s_list = sentence.strip().split()
        if len(s_list) < 5:
            return False, None, None

        e1_id = s_list[0]
        e2_id = s_list[1]
        e1_mention = s_list[2]
        e2_mention = s_list[3]
        label = s_list[4]
        sentence_mention = s_list[5:]

        s = RESentence(sentence_mention, e1_mention, e2_mention, 0, 0, e1_id, e2_id)

        return True, s, label

    def report_multi_label(self):
        """
        查找给定的数据集中一个实体对存在多个关系的比例
        :return:
        """
        count = 0  # 记录有多少个实体对是多关系的
        ml_ht = dict()
        for k, v in self.ht_index.items():

            ht_labels = set([self.labels[sid] for sid in v])

            if len(ht_labels) > 1:
                count += 1
                ml_ht[k] = ht_labels

        print("there are %d entity pairs that have more than one relations" % count)

        return ml_ht


if __name__ == "__main__":
    demo_file = "./train.txt"

    sample_ds = RiedelDataset(demo_file)
    sample_ds.report_multi_label()
    print()
