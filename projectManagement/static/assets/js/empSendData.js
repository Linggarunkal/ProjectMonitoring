$(function(){
    $('#addEmployee').click(function(){
    	event.preventDefault();
       	var form_data = new FormData($('#addEmpNew')[0]);
        $.ajax({
            url: '{{ url_for('empAdd') }}',
            data: $('form').serialize(),
            type: 'POST',
            success: function(data){
                JSalert();
                function JSalert(){
                    swal("Congrats!", " Data Success created to System ", "success")
                    .then(willRedirect => {
                        if (willRedirect){
                            window.location.href = "http://localhost:14045/project/main";
                            }
                    });
                }
            },
            error: function(data){
                console.log(data);
            }
        });
    });
});