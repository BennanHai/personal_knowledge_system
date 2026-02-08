# @Author: Benanahai
# @Time  : 2025/4/27 16:04 
# @Desc  : 探索pyOpenSSL 解析证书内容


from OpenSSL.crypto import load_certificate, FILETYPE_PEM
# 读取证书文件
with open('certificate.pem', 'rb') as f:
    cert_str = f.read()

cert = load_certificate(FILETYPE_PEM, cert_str)

# 主题信息
subject = cert.get_subject()
print("主题信息:")
print("国家: ", subject.C)
print("组织: ", subject.O)
print("CN: ", subject.CN)

# 有效期
not_before = cert.get_notBefore().decode()
not_after = cert.get_notAfter().decode()
print("有效期: ", not_before, " 至 ", not_after)

# 序列号
serial_number = cert.get_serial_number()
print("序列号: ", hex(serial_number))

# 签名算法
signature_algorithm = cert.get_signature_algorithm().decode()
print("签名算法: ", signature_algorithm)

# 公钥信息
public_key = cert.get_pubkey()
public_key_info = public_key.to_cryptography_key()
print("公钥信息:", public_key_info)

