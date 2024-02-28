import qrcode

### Generating study_bear url qr code
study_bear_qr = qrcode.make("https://sakimilo.github.io/winnie_the_study_bear")
study_bear_qr.save("./qrcode_images/study_bear_qr.jpg")

### Generating marketing_persona url qr code
marketing_persona_qr = qrcode.make("https://sakimilo.github.io/marketing_persona")
marketing_persona_qr.save("./qrcode_images/marketing_persona_qr.jpg")

### Generating akinator_magic url qr code
akinator_magic_qr = qrcode.make("https://sakimilo.github.io/akinator_magic")
akinator_magic_qr.save("./qrcode_images/akinator_magic_qr.jpg")

### Generating akinator_multiplayer url qr code
akinator_multiplayer_qr = qrcode.make("https://sakimilo.github.io/akinator_multiplayer")
akinator_multiplayer_qr.save("./qrcode_images/akinator_multiplayer_qr.jpg")