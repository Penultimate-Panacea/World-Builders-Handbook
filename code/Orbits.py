class OrbitTable:
    #  - is inside star, I is inner, H is habitable, O is outer, _ is incinerated, S is the star itself
    table_00 = ["S", "_", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O"]
    table_01 = ["S", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_02 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_03 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_04 = ["S", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_05 = ["S", "-", "-", "_", "_", "_", "_", "I", "I", "I", "I", "H", "O", "O", "O"]
    table_06 = ["S", "-", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_07 = ["S", "-", "-", "-", "-", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_08 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_09 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_0A = ["S", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_0B = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_0C = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_0 = [table_00, table_01, table_02, table_03, table_04, table_05, table_06, table_07, table_08, table_09,
               table_0A, table_0B, table_0C]
    table_10 = ["S", "_", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O"]
    table_11 = ["S", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O", "O"]
    table_12 = ["S", "_", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O"]
    table_13 = ["S", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O"]
    table_14 = ["S", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O"]
    table_15 = ["S", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O"]
    table_16 = ["S", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O"]
    table_17 = ["S", "-", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O"]
    table_18 = ["S", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O"]
    table_19 = ["S", "-", "-", "-", "-", "_", "I", "I", "I", "I", "H", "H", "O", "O", "O"]
    table_1A = ["S", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "O", "O", "O"]
    table_1B = ["S", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "H", "O", "O"]
    table_1C = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "H", "H", "O", "O"]
    table_1 = [table_10, table_11, table_12, table_13, table_14, table_15, table_16, table_17, table_18, table_19,
               table_1A, table_1B, table_1C]
    #  ABOVE COMPLETE TODO BELOW:
    table_20 = ["S", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "O", "H", "O"]
    table_21 = ["S", "_", "_", "_", "_", "I", "I", "I", "I", "I", "I", "I", "O", "O", "O"]
    table_22 = ["S", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O", "O"]
    table_23 = ["S", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O", "O", "O"]
    table_24 = ["S", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O", "O", "O"]
    table_25 = ["S", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O", "O", "O"]
    table_26 = ["S", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O", "O", "O"]
    table_27 = ["S", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O", "O", "O"]
    table_28 = ["S", "_", "I", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O", "O"]
    table_29 = ["S", "-", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O", "O"]
    table_2A = ["S", "-", "-", "-", "I", "I", "I", "I", "I", "I", "H", "O", "O", "O", "O"]
    table_2B = ["S", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "H", "O", "O"]
    table_2C = ["S", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "H", "O", "O"]
    table_2 = [table_20, table_21, table_22, table_23, table_24, table_25, table_26, table_27, table_28, table_29,
               table_2A, table_2B, table_2C]
    table_30 = ["S", "_", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O"]
    table_31 = ["S", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_32 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_33 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_34 = ["S", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_35 = ["S", "-", "-", "_", "_", "_", "_", "I", "I", "I", "I", "H", "-", "O", "O"]
    table_36 = ["S", "-", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_37 = ["S", "-", "-", "-", "-", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_38 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_39 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_3A = ["S", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_3B = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_3C = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_3 = [table_30, table_31, table_32, table_33, table_34, table_35, table_36, table_37, table_38, table_39,
               table_3A, table_3B, table_3C]
    table_40 = ["S", "_", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O"]
    table_41 = ["S", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_42 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_43 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_44 = ["S", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_45 = ["S", "-", "-", "_", "_", "_", "_", "I", "I", "I", "I", "H", "-", "O", "O"]
    table_46 = ["S", "-", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_47 = ["S", "-", "-", "-", "-", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_48 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_49 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_4A = ["S", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_4B = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_4C = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_4 = [table_40, table_41, table_42, table_43, table_44, table_45, table_46, table_47, table_48, table_49,
               table_4A, table_4B, table_4C]
    table_50 = ["S", "_", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O"]
    table_51 = ["S", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_52 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_53 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_54 = ["S", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_55 = ["S", "-", "-", "_", "_", "_", "_", "I", "I", "I", "I", "H", "-", "O", "O"]
    table_56 = ["S", "-", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_57 = ["S", "-", "-", "-", "-", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_58 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_59 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_5A = ["S", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_5B = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_5C = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_5 = [table_50, table_51, table_52, table_53, table_54, table_55, table_56, table_57, table_58, table_59,
               table_5A, table_5B, table_5C]
    table_60 = ["S", "_", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O"]
    table_61 = ["S", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_62 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_63 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_64 = ["S", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_65 = ["S", "-", "-", "_", "_", "_", "_", "I", "I", "I", "I", "H", "-", "O", "O"]
    table_66 = ["S", "-", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_67 = ["S", "-", "-", "-", "-", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_68 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_69 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_6A = ["S", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_6B = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_6C = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_6 = [table_60, table_61, table_62, table_63, table_64, table_65, table_66, table_67, table_68, table_69,
               table_6A, table_6B, table_6C]
    table_70 = ["S", "_", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O"]
    table_71 = ["S", "_", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_72 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_73 = ["S", "-", "_", "_", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_74 = ["S", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_75 = ["S", "-", "-", "_", "_", "_", "_", "I", "I", "I", "I", "H", "-", "O", "O"]
    table_76 = ["S", "-", "-", "-", "_", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_77 = ["S", "-", "-", "-", "-", "_", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_78 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_79 = ["S", "-", "-", "-", "-", "-", "_", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_7A = ["S", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "I", "H", "O", "O"]
    table_7B = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_7C = ["S", "-", "-", "-", "-", "-", "-", "-", "I", "I", "I", "I", "H", "O", "O"]
    table_7 = [table_70, table_71, table_72, table_73, table_74, table_75, table_76, table_77, table_78, table_79,
               table_7A, table_7B, table_7C]
    master_table = [table_0, table_1, table_2, table_3, table_4, table_5, table_6, table_7]


class Orbit:
    def __init__(self):
        self.number = None
        self.is_inner = False
        self.is_hab = False
        self.is_outer = False
        self.is_incinerated = False
        self.body = None
