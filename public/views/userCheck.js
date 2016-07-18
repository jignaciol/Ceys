var ceys = ceys || {}

ceys.views.userCheck = Backbone.View.extend({

    template: _.template( ceys.utils.loadHtmlTemplate("userCheck") ),

    render: function() {
        this.$el.html(this.template())
    },

    initialize: function() {
        this.render()
    }

})
