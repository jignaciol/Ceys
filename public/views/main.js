var ceys = ceys || {}

ceys.views.main = Backbone.View.extend({

    template: _.template( ceys.utils.loadHtmlTemplate("body_wrapper") ),

    render: function() {
        this.$el.html(this.template())
        ceys.app.clock = new ceys.models.clock()
        this.date = new Date()
        this.day = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"],
        this.month = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],

        ceys.app.clock.set({
            hour: this.date.toLocaleTimeString(),
            day: this.date.getDay(),
            weekday: this.day[ this.date.getDay() ],
            month: this.month[ this.date.getMonth() ]
        })
        ceys.app.userCheck = new ceys.views.userCheck({ el: this.$(".usercheck") })
        ceys.app.clockView = new ceys.views.clockView({ el: this.$(".reloj"), model: ceys.app.clock })
    },

    initialize: function() {
        this.render()
    }

})
