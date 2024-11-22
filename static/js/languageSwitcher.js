function changeButtonText(newText) {
    const button = document.getElementById('languageButton');
    button.textContent = newText;
  }
  
  function imgButton(img) {
    const button = document.getElementById('pathIMG');
    button.src = img;
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    const initialLanguage = "{{ lang }}";
  
    const languageMap = {
      "pt_BR": "Português",
      "en": "English",
    };
  
    const flagMap = {
      "pt_BR": "{{ url_for('static', filename='image/br.png') }}",
      "en": "{{ url_for('static', filename='image/us.png') }}",
    };
  
    changeButtonText(languageMap[initialLanguage]);
    console.log(flagMap[initialLanguage])
    imgButton(flagMap[initialLanguage]);
  });
  