from django.shortcuts import render
from railfence_app.railfence import encryptRailFence, decryptRailFence

def railfence_encrypt(request):
    if request.method == 'POST':
        message = request.POST['message']
        key = int(request.POST['key'])
        encrypted_message = encryptRailFence(message, key)
        return render(request, 'encrypt.html', {'message': message, 'key': key, 'encrypted_message': encrypted_message})
    return render(request, 'encrypt.html')

def railfence_decrypt(request):
    if request.method == 'POST':
        encrypted_message = request.POST['encrypted_message']
        key = int(request.POST['key'])
        decrypted_message = decryptRailFence(encrypted_message, key)
        return render(request, 'decrypt.html', {'encrypted_message': encrypted_message, 'key': key, 'decrypted_message': decrypted_message})
    return render(request, 'decrypt.html')
