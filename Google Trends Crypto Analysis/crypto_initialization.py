'''
add something 
'''

class CryptoNode: 
    def __init__(self, val = None, type = 'Root'):
        self._val = val 
        self._type = type 
        self._sub_cats = None # maybe just set to [] 
        # self._volume = None 
    def set_sub_cat(self, new_node):
        if self._sub_cats is None:
            self._sub_cats = []
        # if points to nothing, create array to add pointers 
        x = len(self._sub_cats)
        self._sub_cats.append(x)
        self._sub_cats[x] = new_node 
        # creates additional value size +1 of array, points to new node. 
        # return x 
    def get_sub_cats(self):
        return self._sub_cats
    def get_sub_cat_vals(self):
        ret_arr = [] 
        if self._sub_cats is not None: 
            for node in self._sub_cats:
                ret_arr.append(node._val)
        return ret_arr 
    def get_specific_cat(self, position):
        return self._sub_cats[position]
    def get_val(self):
        return self._val 
    def get_type(self):
        return self._type

def append_date_val_tree(root, data, type):
    type = find_next_type(type)
    if len(data) != 0:
        if root.get_sub_cats() is not None and len(root.get_sub_cat_vals())>0:
            if data[0] in root.get_sub_cat_vals():
                for node in root.get_sub_cats():
                    if data[0] == node.get_val():
                        pass_node = node 
                append_date_val_tree(pass_node, data[1:], type)
            else: # create new node for val 
                new_node = CryptoNode(data[0], type)
                root.set_sub_cat(new_node)
                append_date_val_tree(new_node, data[1:], type)
        else: # create new node for val 
            # print("ELSE HAPPENED")
            new_node = CryptoNode(data[0], type)
            root.set_sub_cat(new_node)
            append_date_val_tree(new_node, data[1:], type)
      

def find_next_type(current):
    if current == 'Root':
        return 'Year'
    elif current == 'Year':
        return 'Month'
    elif current == 'Month':
        return 'Day'
    elif current == 'Day':
        return 'Val'
    else:
        return 'Something went wrong' # ideally remove this 

def convert_val_to_vol(data,volume):
    return round((data/100)*volume, 2)

def create_crypto(dates, vals, volume):
    root = CryptoNode()
    
    for j in range(len(dates)): 
        date = dates[j]
        indv_date = []
        indv_date.append(int(date[-4:]))
        for i in range(len(date)):
            word = date[i]
            if word == '/':
                indv_date.append(int(date[:i]))
                indv_date.append(int(date[i+1:-5]))
                break 
        v = convert_val_to_vol(int(vals[j]), volume)
        indv_date.append(v)
        append_date_val_tree(root, indv_date, root.get_type())
    return root 

def create_crypto_price(dates, price):
    root = CryptoNode()
    
    for j in range(len(dates)): 
        date = dates[j]
        indv_date = []
        indv_date.append(int('20' + date[-2:]))
        for i in range(len(date)):
            word = date[i]
            if word == '-':
                m = str_month_to_int(date[i+1:-3])
                indv_date.append(m)
                indv_date.append(int(date[:i]))
                break 
        # v = convert_val_to_vol(int(vals[j]), volume)
        v = int(price[j])
        indv_date.append(v)
        append_date_val_tree(root, indv_date, root.get_type())
    return root 

def str_month_to_int(month):
    str_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']   
    m = 0 
    for i in range(len(str_months)):
        if month == str_months[i]:
            m = i 
            break 
    return m 


def print_tree(root, count = 0):
    if count == 40:
        return 
    if root.get_sub_cats() is not None:
        for node in root.get_sub_cats():
            if node.get_type() == 'Year':
                print() 
                print("###################################################")
            elif node.get_type() == 'Month':
                print("___________________________________________________")
            print(f"type: {node.get_type()} || val: {node.get_val()} ")
            count += 1 # get rid of count later if u want to test entire tree 
            print_tree(node, count)
            

def convert_to_array(list):
    ret_arr = [] 
    for val in list: 
        ret_arr.append(val)
    return ret_arr 


