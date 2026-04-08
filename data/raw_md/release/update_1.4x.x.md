# - API 변경 내용 -

## 추가 API

#### 고스트 심볼 모델 face의 반사 효과 정도를 지정 API.

> -   bool setModelFaceReflect(string id, unsigned int face_index, float reflect)
> -   Class : JSGhostSymbolMap
> -   Parameter
>     -   id : 모델 ID
>     -   face_index : 효과를 적용할 face 인덱스
>     -   reflect : 반사 효과 정도 (0.0~1.0 사이 값)
> -   [Example](http://sandbox.dtwincloud.com/code/main.do?id=object_ghost_symbol_reflect)

#### Hex code 문자열로 색상 값을 초기화 API( RGB(#RRGGBB) ARGB(#AARRGGBB) 형태로 설정 가능 ).

> -   new Module.JSColor(string \_hexCode)
> -   Class : JSColor
> -   Parameter
>     -   hexCode: 색상 설정 코드 문자열
> -   Example

```javascript
var colorRGB = new Module.JSColor("#FFDB32");
var colorARGB = new Module.JSColor("#AAFFDB32");
```

#### 마우스 피킹 옵션 반환 API.

```javascript
// false : 공간 계산 방식, true : 그래픽 판별 방식
var pickingType = Module.getOption().getPickingCalculateType();
```

## 개선 API

#### 색상 상수 추가

```javascript
// JSColor Before
style.setFillColor(new Module.JSColor(255, 255, 240));
// JSColor After
style.setFillColor(Module.COLOR_IVORY);
```

#### 레이어 타입 상수 추가

```javascript
Module.TILE_LAYER_TYPE_REAL3D;
```

#### 레이어 리스트 반환 API 개선

```javascript
{
// TileLayer Before
var serviceLayerList = new Module.JSLayerList(false);
Module.XDEMapCreateLayer(...);
// TileLayer After
Module.getTileLayerList().createXDServerLayer({...});
}

{
// UserLayer Before
var objectLayerList = new Module.JSLayerList(true);
objectLayerList.createLayer(...);
// UserLayer After
Module.getObjectLayerList().createObjectLayer({...});
}
```

#### 레이어 생성 API 개선

```javascript
{
    // TileLayer Before
    var serviceLayerList = new Module.JSLayerList(false);
    Module.XDEMapCreateLayer(
        "facility_build",
        "http://xdworld.vworld.kr:8080/",
        8080,
        true,
        true,
        false,
        9,
        0,
        15
    );
    // TileLayer After
    Module.getTileLayerList().createXDServerLayer({
        name: "facility_build", // 필수
        url: "http://xdworld.vworld.kr:8080", // 필수
        type: Module.TILE_LAYER_TYPE_REAL3D, // 필수
        visible: false, // 옵션 (default : true)
        selectable: false, // 옵션 (default : true)
        minLevel: 10, // 옵션 (default : 0)
        maxLevel: 14, // 옵션 (default : 15)
    });
}

{
    // UserLayer Before
    var objectLayerList = new Module.JSLayerList(true);
    var layer = objectLayerList.createLayer("layer", Module.ELT_3DPOINT);
    layer.setMinDistance(100.0);
    layer.setMaxDistance(10000.0);
    // UserLayer After
    Module.getObjectLayerList().createObjectLayer({
        name: "facility_build", // 필수
        type: Module.ELT_3DPOINT, // 필수
        visible: false, // 옵션 (default : true)
        selectable: false, // 옵션 (default : true)
        minDistance: 100.0, // 옵션 (default : 0.0)
        maxDistance: 1000.0, // 옵션 (default : 3000.0)
    });
}
```

#### 지도 초기 생성 API 개선

```javascript
//  Before
var Module = {
    // 필요한 Module 옵션
    postRun: [
        function () {
            "기능 초기화";
        },
    ],
    canvas: (function () {
        var canvas = document.createElement("canvas");
        canvas.id = "canvas";
        canvas.width = "calc(100%)";
        canvas.height = "100%";
        canvas.style.position = "fixed";
        canvas.style.top = "0px";
        canvas.style.left = "0px";
        canvas.addEventListener("contextmenu", function (e) {
            e.preventDefault();
        });
        document.body.appendChild(canvas);
        return canvas;
    })(),
};
// 지도 초기화
Module.Start(window.innerWidth, window.innerHeight - 200);

//  After
// HTML 설정
<div id="container" style="position: fixed; width: 100%; height: 100%; z-index: 0"></div>;

// Module 설정
var Module = {
    // 필요한 Module 옵션
    postRun: [
        function () {
            "기능 초기화";
        },
    ],
};

// 지도 초기화
let container = document.getElementById("container");
Module.initialize({
    container: container,
});
```

## 샌드박스 업데이트

> -   [반사 효과](http://sandbox.dtwincloud.com/code/main.do?id=object_ghost_symbol_reflect)
> -   [고스트심볼(Shape)](http://sandbox.dtwincloud.com/code/main.do?id=object_shape_to_ghost_symbol)
> -   [라인 3D(Shape)](http://sandbox.dtwincloud.com/code/main.do?id=object_shape_to_line)
> -   [라인 RTT(Shape)](http://sandbox.dtwincloud.com/code/main.do?id=object_shape_to_line_rtt)
> -   [파이프(Shape)](http://sandbox.dtwincloud.com/code/main.do?id=object_shape_to_pipe)
> -   [POI(Shape)](http://sandbox.dtwincloud.com/code/main.do?id=object_shape_to_poi)
> -   [폴리곤 3D(Shape)](http://sandbox.dtwincloud.com/code/main.do?id=object_shape_to_polygon)
> -   [폴리곤 RTT(Shape)](http://sandbox.dtwincloud.com/code/main.do?id=object_shape_to_polygon_rtt)
> -   [폴리곤 솔리드(Shape)](http://sandbox.dtwincloud.com/code/main.do?id=object_shape_to_polygon_solid)
> -   [고스트심볼(GeoJson)](http://sandbox.dtwincloud.com/code/main.do?id=object_geojson_to_ghost_symbol)
> -   [라인 3D(GeoJson)](http://sandbox.dtwincloud.com/code/main.do?id=object_geojson_to_line)
> -   [라인 RTT(GeoJson)](http://sandbox.dtwincloud.com/code/main.do?id=object_geojson_to_line_rtt)
> -   [파이프(GeoJson)](http://sandbox.dtwincloud.com/code/main.do?id=object_geojson_to_pipe)
> -   [POI(GeoJson)](http://sandbox.dtwincloud.com/code/main.do?id=object_geojson_to_poi)
> -   [폴리곤 3D(GeoJson)](http://sandbox.dtwincloud.com/code/main.do?id=object_geojson_to_polygon)
> -   [폴리곤 RTT(GeoJson)](http://sandbox.dtwincloud.com/code/main.do?id=object_geojson_to_polygon_rtt)
> -   [폴리곤 솔리드(GeoJson)](http://sandbox.dtwincloud.com/code/main.do?id=object_geojson_to_polygon_solid)
> -   [DEM 단면 그래프](http://sandbox.dtwincloud.com/code/main.do?id=terrain_dem_slice)
> -   [건물 단면 그래프](http://sandbox.dtwincloud.com/code/main.do?id=layer_building_altitude_slice)
> -   [가로수 라인 배치](http://sandbox.dtwincloud.com/code/main.do?id=object_ghostsymbol_positioning_line)
> -   [가로수 영역 배치](http://sandbox.dtwincloud.com/code/main.do?id=object_ghostsymbol_positioning_area)
> -   [교통](http://sandbox.dtwincloud.com/code/main.do?id=effect_traffic)

# - 업데이트 내역 -

## 1.49.2 Hotfix (2023/04/07)

> -   엔진 실행 중 defaultKey 입력 시 반드시 암호화 된 키 사용
>     -   스크립트 파일 상 키 노출이 되지 않도록 defaultKey 입력 시 반드시 암호화 된 키를 사용하도록 변경되었습니다.

## 1.49.1 Hotfix (2023/04/06)

> -   MML_RETURN_ANALYSISPOS 마우스모드 랜더링 오류 수정

## 1.49.0 (2023/04/04)

> -   시곡면 분석 각도 적요 오류 수정
> -   전광판 (CJSFigure) 편집 오류 수정
> -   파이프 애니메이션 오류 수정
> -   고스트심볼 편집 오류 수정

## 1.48.0 (2023/03/24)

> -   마우스 피킹 방법 설정 옵션 값 반환 API가 추가되었습니다.
> -   xdo 모델 불러오기 중 발생하는 오류가 수정되었습니다.

## 1.47.0 (2023/03/13)

> -   JSObject setPickable 기능 복구
> -   가시권분석3D 지형 분석 추가
>     -   Module.getAnalysis().setTerrainAnalysis(true); // 지형 분석 여부 설정
> -   IndexedDB API 추가
>     -   Module.getOption().setIndexedDB(true); // IndexedDB 사용 여부 설정
>     -   Module.getOption().setMaxIndexedDB(15); // IndexedDB 활용 최고 레벨 설정

## 1.46.0 (2023/02/22)

> -   JSPoint property z_index 기능 추가 완료
>     -   그리기 순서 변경 기능 (입력값이 클수록 상위로 작을수로 하위로 가시화)

## 1.45.0 (2023/02/15)

> -   모바일에서 지도가 멈추는 현상 수정완료
> -   폴리곤 외각선 색상 변경 모듈 수정완료
> -   JSObject 클래스 setSelectable API 수정완료
> -   TileObject 버전별 데이터 가시화 모듈 개발완료
> -   마우스 선택모드 기능 개발완료
>     -   MML_SELECT_RECT
>     -   MML_SELECT_POLY
> -   HTMLObject 분할화면 모듈 개발완료
>     -   HTMLObject는 HTML Element에 종속적으로 개발자가 지정된 left, top을 기준으로 출력 좌표 연산 모듈이 추가
>     -   추후 샌드박스 업로드 예정

## 1.44.0 (2023/01/18)

> -   오브젝트 선택 시 출력되는 색상을 설정할 수 있도록 JSOption에 프로퍼티 가 추가되었습니다.

```javascript
Module.getOption().selectColor = Module.COLOR_YELLOW;
```

## 1.43.0 (2023/01/11)

> -   지도 생성 초기에 호출되는 초기화 API Module.Start를 Module.initialize 로 개선
>     -   기존 Start와 변경된 점
>     -   기존 Start API는 canvas를 매칭하여 canvas에 지도를 렌더링 하였으나, 개선 된 initialize API 에서는 div를 매칭하여 div 내부에 지도 canvas를 자동으로 생성하도록 변경되었습니다.
>     -   div로 지도 화면을 매칭하는 경우 아래와 같은 장점이 있습니다.
>         -   별도 canvas를 만드는 과정이 생략됨.
>         -   마우스 클릭 시 이격 현상이 일어나는 것을 방지함.
>         -   HTML Div Object 관리가 용이함.
>     -   기존 Start API는 화면의 가로, 세로 크기만 설정이 가능하였으나, initialize API에서는 div 뿐만 아니라 canvas id, 지형 URL 설정 등 복합적인 옵션 적용이 가능하도록 개선되었습니다
>     -   Module.Resize API 실행 시 종전에는 canvas 크기에 뷰포트를 맞추어 변경하였으나, div로 설정 시 div 크기에 맞추어 뷰포트가 설정됩니다.
> -   JSPoint 이미지 스케일 설정 프로퍼티 추가
>     -   JSPoint에 이미지 스케일 설정을 위한 프로퍼티 image_scale이 추가되었습니다.
>     -   디폴트 값은 1.0 이며, 이 때 원본 이미지 크기로 렌더링 됩니다.

```javascript
point.image_scale = 0.5;
```

![](../../.gitbook/release_note/1.4/poi_resize.png)

## 1.42.1 Hotfix (2023/01/06)

> -   JSLayerList 클래스의 SyncLayer API 호출 시 오류 발생 문제 수정

## 1.42.0 (2023/01/04)

> -   엔진 초기 로드 시간 단축 및 경량화
> -   MapBox, ArcMap 요청 URL 업데이트

## 1.41.0 (2022/12/28)

> -   레이어 리스트 반환 기능 추가
>     -   레이어 리스트를 매번 생성하지 않고 Module API를 통해 반환 가능
>     -   true, false로 구분하던 레이어 타입 설정 방식을 API 명칭으로 구분 가능하도록 개선
> -   레이어 생성 API 개선
>     -   타일 레이어 생성 XDEMapCreateLayer API의 파라미터가 많아 사용이 불편한 점 보완
>     -   레이어 생성 시 옵션 값은 선택적으로 적용할 수 있도록 보완
>     -   타일 레이어 타입 상수 추가
> -   [오브젝트 레이어에서 setMinDistance/setMaxDistnace 값이 적용되지 않는 현상 수정](https://github.com/EgisCorp/XDWorld/issues/247)
> -   셰이더 warning 메시지 제거
> -   건물 심플 모드 렌더링 예외처리 추
> -   JSColor에 적용할 색상 상수 값 추가

## 1.40.0 (2022/12/21)

> -   엔진 로드 시 출력되는 콘솔 메시지 간략화
> -   고스트 심볼 Face 반사 효과 지정 API 추가
> -   Hex Code 문자여로 색상값 지정 기능 추가
