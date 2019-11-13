$("#addfood").click(function () {
    $.ajax({
        url: "/addfood",
        type: "POST",
        data: {
            a: $('#foodname').val(),
            pro: $("#P").val(),
            car: $("#C").val(),
            fat: $("#F").val(),
            volumep: $("#example2").val(),
            volumec: $("#example2-2").val(),
            volumef: $("#example2-3").val()
        },
        success: function (data) {
            swal("สำเร็จ", "เพิ่มเมนูโปรดเรียบร้อย", "success");
            console.log(data.A)
        }
    })
}),
$("#foodtable").click(function () {
    window.location.replace("http://localhost:8000/foodtable");
});