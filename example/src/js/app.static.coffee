app = angular.module 'example.app.static', []

app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
    $scope.posts = [
        author:
            username: 'Jose'
        title: 'Exemplo #1'
        body: 'Primeiro post estático'
    ,
        author:
            username: 'Karina'
        title: 'Exemplo #2'
        body: 'Novo post estático'
    ]
]
