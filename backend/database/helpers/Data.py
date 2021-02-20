


class DataHelper:

    # def __init__(self):


    def row_to_dict(self, row):
        dic = {}
        for column in row.__table__.columns:
            dic[column.name] = str(getattr(row, column.name))
        return dic

    
    
