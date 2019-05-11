document.addEventListener('DOMContentLoaded', function(){

    class Calender{
        constructor(){
            this.num_daysinview=7;
            this.week_index = 0;
            this.week = moment().startOf('isoWeek');
            this.dow = {};
            this.startofweek = this.week.clone()
            this.endofweek = this.startofweek.clone().add(this.num_daysinview-1,'days')
            this.change_dates();
            
        }

        init_view(week_dates){

            var create_reservation = this.create_reservation;

            $('.col-date').selectable({
                        stop: function() {
                            var times = [];
                            var date = week_dates[this.id];
                            $( ".ui-selected", this ).each(function() {
                                var cell = $('#'+this.id.replace(':','\\:'));
                                if(cell.hasClass('noselect')==true){
                                   times.push(this.id.split("-")[1]);
                                }
                            });
                            create_reservation(date,times);    
                    },
            });
        }

        change_dates(){

            var week_ = this.week.clone().add(this.week_index,'week');
            this.startofweek = week_.clone();
            this.endofweek = week_.clone().add(this.num_daysinview-1,'days');

            document.getElementById("month-tag").innerHTML = week_.format('MMMM YYYY')
            document.getElementById("date-day-label-0").innerHTML = week_.format('ddd MMM Do');
            
            for(var i = 0; i < this.num_daysinview; i++){
                var _date = week_.clone().add(i, 'days');
            document.getElementById("date-day-label-"+i).innerHTML = _date.format('ddd MMM Do');
            this.dow['day-'+i] = _date.format('YYYY-MM-DD');
            }    
            this.get_reservations(this.startofweek,this.endofweek);
            this.init_view(this.dow);
        }

        prev_view(){
            this.clear_reservations();
            this.week_index -= 1;
            this.change_dates();
        }

        next_view(){
            this.clear_reservations();
            this.week_index += 1;
            this.change_dates();
        }

        get_reservations(startdate,enddate){
            var address = window.location.pathname+'/dates/?startdate=' + startdate.format('YYYY-MM-DD')+'&enddate='+enddate.format('YYYY-MM-DD');
            get_jsondata(address,this.display_reservations); 
        }

        display_reservations(data){
            var current_reservations={};
            var reservations = JSON.parse(data);
            for(var i =0; i<reservations.length;i++){
                var reservation = new Reservation(reservations[i].pk,reservations[i].user_id,reservations[i].date,reservations[i].time_start,reservations[i].time_end);
                current_reservations[reservations[i].pk] = reservation;
            }
        } 
    
        delete_reservation(reservation_id){
            var url = window.location.pathname+'/delete-reservation/?reservation_id='+reservation_id;
            var data = {};
            var reservation = $('#'+reservation_id);
            data['reservation_id'] = reservation_id;
            post_data(url,data,destroy_elt);
        }

        create_reservation(date,times){
            var url = window.location.pathname;
            var data = {};
            data['date'] = date;
            data['time_start'] = times[0];
            data['time_end'] = times[times.length-1];

            post_data(url,data,fc.display_reservations);
        }

        clear_reservations(){
            var reservations = document.getElementsByClassName("reservation-date");
            while(reservations[0]){
                reservations[0].parentNode.removeChild(reservations[0]);
            }
            this.current_view_reservations = {};
        }
    }

    class Reservation{
        constructor(pk,username,date,time_start,time_end){
            this._pk = pk;
            this._username = username;
            this._date = date;
            this._time_start = time_start;
            this._time_end = time_end;
            this.render_reservation();
        }

        render_reservation(){
            var reservation_id = '#'+ this._pk;
            for(var i = 0; i < fc.num_daysinview; i++){
                var date = fc.startofweek.clone().add(i,'days').format('YYYY-MM-DD');
                if(this._date == date){
                    var datetime_cell_pos = $('#'+this._time_start.substr(0,5).replace(':','\\:')).parent().offset();
                    var reservation_start_time = parseInt(this._time_start.substr(0,2));
                    var reservation_end_time = parseInt(this._time_end.substr(0,2));
                    var length_of_reservation = reservation_end_time - reservation_start_time;

                    //find and add div element for reservation
                    var element = document.getElementById('day-'+i);
                    var reservation_date_div = elt("div",{class:"reservation-date", id:this._pk});
                    var reservation_time_div = elt("div",{class:"reservation-time",id:("time-" + this._pk)});
                    var btn_delete_reservation = elt("button",{type:"button",id:"delete_"+this._pk, class:"close"});
                    var label_username = elt("p",{id:"user",class:"reservation-user-label"},this._username);
                    
                    btn_delete_reservation.innerHTML = '&times;';
                    btn_delete_reservation.addEventListener("click",function(){fc.delete_reservation(btn_delete_reservation.id.split("_")[1])});

                    reservation_time_div.appendChild(btn_delete_reservation);
                    reservation_time_div.appendChild(label_username);
                    reservation_date_div.appendChild(reservation_time_div);
                    element.appendChild(reservation_date_div);

                    $("#time-" + this._pk).height(30*(length_of_reservation+1));
                    $(reservation_id).offset({top: datetime_cell_pos.top});
                    break;
                }
            }
        }
    }

    function inst_eventListeners(){
        document.getElementById("btn-week-prev").addEventListener("click", function(){fc.prev_view()});
        document.getElementById("btn-week-next").addEventListener("click", function(){fc.next_view()});
    }

    fc = new Calender()
    
    inst_eventListeners();

});


