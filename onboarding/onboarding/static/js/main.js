// Author: Ajith VM

$(document).ready(function () {
  $('body .fancyRadioButtons .controls .checkbox').each(function (index, item) {
    var thisRadio = $(this).find('input')
    var value = $(thisRadio).prop('value')
    var name = $(thisRadio).prop('name')
    var id = $(thisRadio).prop('id')
    $(item).html(
      '<input type="checkbox" value="' +
        value +
        '" id="' +
        id +
        '" name="' +
        name +
        '"></input><span>' +
        value +
        '</span>'
    )
  })
  $('body #fancySelect').each(function () {
    var parentSelect = $(this)
    $(parentSelect)
      .find('select option')
      .each(function (index, item) {
        var mainSelect = $(parentSelect).find('select')
        var id = 'option' + $(mainSelect).attr('id') + index
        var text = $(item).html()
        $(this)
          .parent()
          .parent()
          .parent()
          .append(
            '<div class="fancySelectBox" id="' + id + '">' + text + '</div>'
          )
        $('#' + id)
          .unbind()
          .clearQueue()
          .bind('click', function () {
            $(mainSelect).prop('value', $(this).html())
            $(this)
              .parent()
              .find('.fancySelectBox')
              .removeClass('active')
            $(this).addClass('active')
          })
        if ($(mainSelect).prop('value') === text) {
          // selecting current active
          $('#' + id).addClass('active')
        }
      })
  })
})
