(function($) {

    ceys.routers.ceysRouter = Backbone.Router.extend({

        routes:{
            "": "showInit"
        },

        showError: function(){
        },

        showInit: function() {
            ceys.app.main = new ceys.views.main({
                el: $(".mainWrapper")
            })
        },

    })

    var CeysApp = new ceys.routers.ceysRouter()

    this.day = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"],
    this.month = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],

    setInterval(function () {
        this.date = new Date()

        ceys.app.clock.set({
            hour: this.date.toLocaleTimeString(),
            day: this.date.getDay(),
            weekday: this.day[ this.date.getDay() ],
            month: this.month[ this.date.getMonth() ]
        })
    }, 1000)

    Backbone.history.start()
})(jQuery)
