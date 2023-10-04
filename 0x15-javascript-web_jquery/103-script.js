$('document').ready(function () {
  $('INPUT#btn_translate').on('click', translate);
  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      translate();
    }
  });
  function translate (e) {
    const lan = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lan, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
});
