(($) ->
  class Utilities
    makeChart: (container, highChartsData) ->
      $(container).highcharts highChartsData


    initializeLobiPanel: ->
      $('#lobipanel-multiple').find('.panel').lobiPanel
        sortable: true
        reload: false
        editTitle: false
        unpin: false
        minimize: false


    addTile: (postCodes, type) =>
      $.ajax
        url: '/getTile/'
        method: 'GET'
        data: {postCodes, type}
        contentType: 'application/json'
        success: (htmlCode) =>
          newTile = $ htmlCode
          $('#first_col').prepend newTile
          @initializeLobiPanel()


  $.utilities = new Utilities()
) jQuery
