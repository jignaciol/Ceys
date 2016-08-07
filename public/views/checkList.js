var ceys = ceys || {}

ceys.views.checkList = Backbone.View.extend({

    template: _.template( ceys.utils.loadHtmlTemplate("checkList") ),

    render: function() {
        this.$el.html(this.template())
    },

    initialize: function() {
        this.render()
    }

})
