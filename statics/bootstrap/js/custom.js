
$(document).ready(function () {
    $("#jsStayBtn").on('click', function () {
        $.ajax({
            cache: false,
            type: "POST",
            url: "/add_comment/",
            data: $('#jsStayForm').serialize(),
            dateType: "json",
            async: true,
            // beforeSend: function (xhr, settings) {
            //     xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
            // },
            success: function(data) {
                if(data.status == 'success'){
                    alert("提交成功");
                     window.location.reload();//刷新当前页面.
                }else if(data.status == 'fail'){
                    alert("评论错误，请重新评论");
                }
            },
        });
    });
});

