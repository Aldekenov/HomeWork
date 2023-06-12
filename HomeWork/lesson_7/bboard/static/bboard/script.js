$('#Form').validate({
      rules: {...},
      message: {...},
      errorPlacement: function(error, element) {
            if (element.type == 'checkbox') {
                error.appendTo(element.parent());
            }
            else {
                error.insertAfter(element);
            }
        }
});