$(document).ready(function () {
  // Add click event listener to the translate button
  $('#btn_translate').click(function () {
    // Get the language code from the input field
    const languageCode = $('#language_code').val();

    // Construct the API URL with the language code
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;

    // Make an AJAX GET request to the API
    $.get(apiUrl, function (data) {
      // Update the #hello div with the translated greeting
      $('#hello').text(data.hello);
    });
  });
});
