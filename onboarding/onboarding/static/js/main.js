// Author: Ajith VM

$(document).ready(function () {
  $('body #fancySelect').each(function () {
    var parentSelect = $(this);
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
