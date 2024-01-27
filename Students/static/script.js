
var toggle=true, tb=true



$("#toggle-table").on("click",()=>{
  var table=$("#course-table")
    if(tb){
        $("#toggle-table").removeClass("fa-tbl-h")
        $("#toggle-table").addClass("fa-tbl")
        table.css({"transition":"all 0.5s ease"})
        table.css({"display":"none","overflow":"visible"})
         
    }
    else{
        $("#toggle-table").addClass(".fa-tbl-h")
        $("#toggle-table").removeClass("fa-tbl")
        table.css({"display":"table","overflow":"visible"})
        
    }
    tb=!tb

})
function toggler(toggle){
    $(".menu").on("click",(e)=>{
       if (toggle){ 
         $(".menu").attr("name","menu-outline")
         toggle=false
         $(".sidebar").toggleClass("active")
        }
        else{
           
         $(".menu").attr("name","close-outline")
         toggle=true
         $(".sidebar").toggleClass("active")
        }
     })

}

$(document).ready(()=>{
    toggler(toggle)

})


var displayAlert=(item,text,is_error)=>{
    if(is_error){
        item.addClass("btn-danger")
        item.html(text)
        item.removeClass("hide")

    }
    else{
        item.html(text)
        item.addClass("btn-success")
        item.removeClass("hide")

    }
    var interval=setTimeout(()=>{
        item.html("")
        item.removeClass("btn-danger")
        item.removeClass("btn-success")
        item.addClass("hide")


    },3000)
}
$(document).ready(()=>{
    var alerter=$("#alerter")
    $(".form-lipa").on("submit",(e)=>{

        e.preventDefault()

        var amount=$("#amount").val()
        var phone=$("#number").val()

        if (amount =="" || amount == "0"){
            
            displayAlert(alerter,"0 amount not allowed",true)
        }
        else{

            $.ajax({
                type:"post",
                url:"/lipa",
                data:{"amount":amount,"phone":phone},
                success:(data)=>{
                    response=JSON.parse(data)
                    console.log(data)
                    displayAlert(alerter,data,false)
                },
                error:(error)=>{
                    displayAlert(alerter,"Error processing",true)
                }
            })
        }


    })
})

$("#search").on("change",(e)=>
{
    var prog=$("#course-query").val()
    var search=$("#search").val()
    console.log("changing")
    fetch_students(search,prog)


})

function fetch_students(search,prog){

    $.ajax({
        type:"post",
        url:"/students/all",
        data:{"prog":prog,"search":search},
        success:(data)=>{
            students=JSON.parse(data)
            $("#student-data").html("")
            if (students.length ==0){
                $("#student-data").append(`<tr>
                <td colspan='6'> <div class="alert alert-danger text-center">No students found </div></td>
                `)
            }
            students.forEach(student => {
                fields=student.fields
                
                var adm=student['pk']
                
                $("#student-data").append(`<tr>
                <td>${fields.student_no}</td>
                <td>${fields.surname}</td>
                <td>${fields.othernames}</td>
                <td>${fields.email}</td>
                <td>${fields.phone_number}</td>
                <td>${fields.prog_code}</td>
                <td class="d-flex">
                <button class="btn text-success p-0"  type="button"  data-bs-toggle="modal" data-bs-target="#student${ fields.phone_number }">
                                <i class="fa fa-eye fa-sm" aria-hidden="true"></i>
                              </button>     
                  <div class="modal" id="student${fields.phone_number}" tabindex="-1" aria-labelledby="mymodallabel1" aria-hidden="false">
                    <div class="modal-dialog" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <p class="modal-title align-items-center">
                                Record for ${fields.surname}</p>
                                <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="close">
                                    <span aria-hidden="true"></span>
                                </button>
                            </div>
                            <div class="modal-body">
                              <div class="card">
                                <div class="card-content">
                                  <div class="card-body">
                                    <div class="card-text border rounded d-flex flex-column justify-content-center">
                                      <div class="text-center p-3">

                                      
                                      <img src="/media/${fields.image}" class="profile_image border" alt="" srcset="">
                                    </div>

                                      <table class="table table-responsive">

                                        <tbody>
                                          <tr class="mt-2">
                                            <th class="me-2">Student No</th>
                                            <td>${fields.student_no}</td>
                                          </tr>
                                          <tr class="mt-2">
                                            <th class="me-2">Full Names </th>
                                            <td>${fields.surname} ${fields.othernames}</td>
                                          </tr>
                                          <tr class="mt-2">
                                            <th class="me-2">Email </th>
                                            <td>${fields.email}</td>
                                          </tr>

                                          <tr class="mt-2">
                                            <th class="me-2">Course </th>
                                            <td>${fields.prog_code}</td>
                                          </tr>
                                          <tr class="mt-2">
                                            <th class="me-2">Mobile </th>
                                            <td>${fields.phone_number}</td>
                                          </tr>
                                          <tr class="mt-2">
                                            <th class="me-2">Photo url </th>
                                            <td><a href="/media/${fields.image}" class="nav-link" target="_blank">${fields.image.url}</a></td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </div>

                                  </div>
                                </div>
                              </div>
                             

                            </div>
                        </div>

                    </div>

                </div>

                
                <button class="btn btn-light text-success p-0 mx-2"> <a href="../student/edit/${adm}" class=""><i class="fa fa-eye"></i></a>  </button>
        
                 <button class="btn text-danger  p-0 mx-2" data-bs-target="#delstudent${fields.phone_number}" data-bs-toggle="modal"> <i class="fa fa-trash"></i></button>
                   
                 <div class="modal" role="modal" id="delstudent${fields.phone_number}">
                   <div class="modal-dialog" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <p class="modal-title">A you sure you want to delete Student </p>
                        <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true"></span>
                      </button>
                      </div>
                      <div class="modal-body">
                        <div class="modal-text">
                          <p>${fields.surname} ${fields.othernames}</p>
                        </div>
                      </div>

                      <div class="modal-footer">
                        <button  class="btn btn-danger"> <a href="../student/delete/${adm}" class="nav-link text-white">DELETE</a></button>
                        <button class="btn btn-warning" data-bs-dismiss="modal">CANCEL</button>
                      </div> 
                    </div>
                   </div>
                 </div>

              </td>

                </tr>`
                   
                )
                
            });

        },
        error:()=>{
            console.log("Something went wrong")
        }

    })

}
var query_select=$("#course-query")
query_select.on("change",()=>{
    var prog=$("#course-query").val()
    var search=$("#search").val()

    fetch_students(search,prog)
   
})

function hello()
{
  alert("hello james")
}

var canvas1=$("#pie-details")
DrawChart(canvas1,"pie")

DrawChart($("#bar-graph"),"bar")
function DrawChart(ctx,typ){

  

  new Chart(ctx, {
    type: typ,
    data: {
      labels: [2015,2016,2017,2018,2019,2020,2022,2023],
      datasets: [{
        label: 'Number of students Admitted',
        data: ["{{details.student.count}}",300,250,320,400,230,330,400],
        backgroundColor:["red","green","blue","indigo","brown","cyan","orange","magenta"],
        borderWidth: 1
      }]
    }
   
  });
}



