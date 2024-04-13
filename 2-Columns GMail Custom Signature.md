# Customizing your signature for GMail App (mobile/desktop) (a 2-column example)
by [JRM Garcia](https://garcia-inpe.github.io/) / [INPE](https://www.gov.br/inpe/pt-br) / [MCTI](https://www.gov.br/mcti/pt-br), adapted from [https://www.youtube.com/@ShawhinTalebi](https://www.youtube.com/watch?v=NjMD1bGBNqw&list=PLz-ep5RbHosXORBcWr6dy3-Wdq9RT2n2f)

| <span style="font-size:2em;">Observations</span> | <span style="font-size:2em;">Example</span>  |
|-------------|-------------|
|<ul><li>Is the text that presents yourself as a professional/person.</li><li>A fast way to show contact information.</li><li>Usually placed at the end of messages.</li><li>Prevents from setting at every computer/mail computer program.</li><li>Making a 2-column signature is tricky!</li><li>This works only for the GMail App (mobile ou desktop)</li></ul> | ![Example of a 2-column signature](/assets/img/SignatureExample.png)         |

`1. GMail / Setting / See All Settings / No signatures (or signatures) / Create New / Name it and Create`
* The signature editor opens, but with the 1-column default layout….but we want two columns.
* The tricky is to build the layout in Google Sheets ... but only the table structure is leveraged.

`2. Go to Google Sheets and create a similar structure`
* The idea is to copy the 2 columns and paste them in the GMail Signature Editor.
* Contents in Sheets will not be leveraged in the signature editor, only the layout (width, lenght, colors, etc).
* The text and image will be replaced (because its format becomes terrible after pasted).
* Column width and line height matter, the layout will be pasted in the Signature Editor as it is in Sheets.
* The text in Sheets must not be ok when pasted, keep it short and change in the Editor.
* Make columns large enough to fit the desired image and text.
* Create an ~100x100px image in local computer.
* Insert the image OVER the cells in Sheets (to keep its size).
* Adjust the margins and alignment of the cell.
* Background and border line colors are also pasted, format them in Sheets.
* Copy the two columns and paste them in the Signature Editor.<br>
![Example of a Google Sheets layout for GMail 2-column signature](/assets/img/SignatureLayoutInGoogleSheets_v3.png)


`3. Explore the Signature Editor - Try to build something similar to this.`<br><br>
![Example of a Signature](/assets/img/SignatureReady.png)
* You can include links for social media.
* Logos can bem uploaded or captured from provirders like [this one](https://exclaimer.com/email-signature-handbook/social-media-icons-in-email-signatures/).
* One can use HTML editor like [this](https://html-online.com/) in order to build the signature and then paste the design (not the HTML) into the GMail Signature Editor. [Source](https://www.wisestamp.com/guides/gmail-html-signature/#:~:text=Can%20you%20use%20HTML%20in,the%20HTML%20into%20Gmail's%20settings.).
* OBS

Troubleshooting
* [What if I get 'Email signature is too long error?](https://support.google.com/mail/thread/213646412/email-signature-with-any-images-is-too-long?hl=en)
