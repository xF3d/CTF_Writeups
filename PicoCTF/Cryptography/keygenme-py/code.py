import hashlib

bUsername_trial = b"MORTON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"

x = hashlib.sha256(bUsername_trial).hexdigest()

key_part_dynamic1_trial = x[4] + x[5] + x[3] + x[6] + x[2] + x[7] + x[1] + x[8]

key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

print(key_full_template_trial)