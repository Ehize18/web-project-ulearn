import pandas as pd

sby = pd.read_csv("main/static/main/data/salary_by_year", index_col=0)
cby = pd.read_csv("main/static/main/data/count_by_year", index_col=0)


def get_context_dict(temp_dct):
    result = {}
    for d in temp_dct:
        for k1 in temp_dct[d]:
            if pd.isnull(temp_dct[d][k1]):
                temp_dct[d][k1] = "Нет данных"
            else:
                temp_dct[d][k1] = int(float(temp_dct[d][k1]))
            if k1 in result.keys():
                result[k1].append(temp_dct[d][k1])
            else:
                result[k1] = [temp_dct[d][k1]]
    return result


sby_dct = get_context_dict(sby.to_dict())
cby_dct = get_context_dict(cby.to_dict())
