$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lan, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
