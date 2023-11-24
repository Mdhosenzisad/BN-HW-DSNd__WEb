
import pickle
from sklearn.preprocessing import LabelBinarizer

# Your classes or labels
classes = ['Bagerhat', 'Bandarban', 'Barguna', 'Barishal', 'Bhola', 'Bogura', 'Brahmanbaria', 'Chandpur', 'Chittagong', 'Chuadanga', 'CoxsBazar', 'Cumilla', 'Dhaka', 'Dinajpur', 'Faridpur', 'Feni', 'Gaibandha', 'Gazipur', 'Gopalganj', 'Habiganj', 'Jamalpur', 'Jashore', 'Jhalokati', 'Jhenaidah', 'Joypurhat', 'Khagrachhari', 'Khulna', 'Kishoreganj', 'Kurigram', 'Kushtia', 'Lakshmipur', 'Lalmonirhat', 'Madaripur', 'Magura', 'Manikganj', 'Meherpur', 'Moulvibazar', 'Munshiganj', 'Mymensingh', 'Naogaon', 'Narail', 'Narayanganj', 'Narsingdi', 'Natore', 'Nawabganj', 'Netrokona', 'Nilphamari', 'Noakhali', 'Pabna', 'Panchagarh', 'Patuakhali', 'Pirojpur', 'Rajbari', 'Rajshahi', 'Rangamati', 'Rangpur', 'Satkhira', 'Shariatpur', 'Sherpur', 'Sirajganj', 'Sunamganj', 'Sylhet', 'Tangail', 'Thakurgaon']

# Create a LabelBinarizer instance
label_binarizer = LabelBinarizer()
label_binarizer.classes_ = classes

# Specify the file path for the pickle file
file_path = 'Dislabel_binarizer.pkl'

# Save the LabelBinarizer object to a pickle file
with open(file_path, 'wb') as file:
    pickle.dump(label_binarizer, file)

print("LabelBinarizer object saved to:", file_path)

# import pickle
# import pickle
# from sklearn.preprocessing import LabelBinarizer
#
# # Specify the file path of the pickle file
# file_path = 'label_binarizer.pkl'
#
# # Load data from the pickle file
# with open(file_path, 'rb') as file:
#     loaded_data = pickle.load(file)
#
# # Check if the loaded_data is a LabelBinarizer instance
# if isinstance(loaded_data, LabelBinarizer):
#     print("Classes:", loaded_data.classes_)
# else:
#     print("Loaded Data:", loaded_data)
#
# # Print the type of loaded data
# print("\nType of loaded_data:", type(loaded_data))
#
# # Specify the file path of the pickle file
# file_path = 'label_binarizer.pkl'
#
# # Load data from the pickle file
# with open(file_path, 'rb') as file:
#     loaded_data = pickle.load(file)
#
# # Check if the loaded_data is a LabelBinarizer instance
# if isinstance(loaded_data, LabelBinarizer):
#     print("Classes:", loaded_data.classes_)
# else:
#     print("Loaded Data:", loaded_data)
#
# # Print the type of loaded data
# print("\nType of loaded_data:", type(loaded_data))
