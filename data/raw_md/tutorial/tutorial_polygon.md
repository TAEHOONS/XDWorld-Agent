# 폴리곤 생성하기

입력한 좌표를 기반으로 폴리곤을 생성하는 방법에 대해 소개합니다.

## 폴리곤 생성하기

폴리곤은 특정 좌표를 입력받아 [JSPolygon](../object/jspoygon.md) 오브젝트를 이용해 생성합니다.

폴리곤은 아래 단계를 거쳐 가시화 할 수 있습니다.

1. 폴리곤 오브젝트 생성
2. 폴리곤 형태 지정
3. 폴리곤 속성 지정
4. 레이어에 폴리곤 저장

폴리곤으로 입력되는 좌표는 모두 폐곡선을 이루며 분리 된 폴리곤은 Part로 구분합니다.

Part 구성에 따라 여러가지 형태로 구성됩니다.

|                 한 파트의 폴리곤                 |                 여러 파트의 폴리곤                 |               홀(Hole)이 있는 폴리곤              |
| :---------------------------------------: | :----------------------------------------: | :----------------------------------------: |
| ![](<../.gitbook/assets/polygon (1).png>) | ![](<../.gitbook/assets/polygon0 (1).png>) | ![](<../.gitbook/assets/polygon1 (1).png>) |

아래는 폴리곤 오브젝트를 생성하는 전체 코드입니다.

```javascript
function createPolygon() {
    // 1. 폴리곤 객체 생성
    var polygon = Module.createPolygon("MY_POLYGON");

    // 2. 좌표, 파트 설정
    var vertex = new Module.JSVec3Array();
    vertex.push(new Module.JSVector3D(126.9288, 37.526449, 15.0));
    vertex.push(new Module.JSVector3D(126.927471, 37.525806, 15.0));
    vertex.push(new Module.JSVector3D(126.928596, 37.5246, 15.0));
    vertex.push(new Module.JSVector3D(126.929996, 37.525416, 15.0));

    var part = new Module.Collection();
    part.add(4);

    polygon.setPartCoordinates(vertex, part);

    // 3. 폴리곤 색상 설정 (선택)
    var polygonStyle = new Module.JSPolygonStyle();

    polygonStyle.setFill(true);
    polygonStyle.setFillColor(new Module.JSColor(255, 0, 0));

    polygonStyle.setOutLine(true);
    polygonStyle.setOutLineWidth(2.0);
    polygonStyle.setOutLineColor(new Module.JSColor(0, 0, 255));

    polygon.setStyle(polygonStyle);

    // 5. 레이어에 폴리곤 저장
    var layerList = new Module.JSLayerList(true);
    var layer = layerList.createLayer("POLYGON_LAYER", Module.ELT_POLYHEDRON);
    layer.addObject(polygon, 0);
}
```

이어서 코드의 세부 단계에 대해 알아봅니다.

### step 1. 폴리곤 오브젝트 생성

Module을 통해 [JSPolygon](../object/jspolygon.md) 타입의 폴리곤 오브젝트를 생성합니다.

```javascript
var polygon = Module.createPolygon("MY_POLYGON");
```

### step 2. 폴리곤 형태 지정

폴리곤의 형태를 지정하기 위해 좌표와 파트 정보를 추가합니다.

```javascript
var vertex = new Module.JSVec3Array();
vertex.push(new Module.JSVector3D(126.9288, 37.526449, 15.0));
vertex.push(new Module.JSVector3D(126.927471, 37.525806, 15.0));
vertex.push(new Module.JSVector3D(126.928596, 37.5246, 15.0));
vertex.push(new Module.JSVector3D(126.929996, 37.525416, 15.0));

var part = new Module.Collection();
part.add(4);

polygon.setPartCoordinates(vertex, part);
```

폴리곤은 기본적으로 폐곡선 형태로 이루어지며, 좌표의 방향에 따라 외부와 내부가 구분됩니다.

![](<../.gitbook/assets/polygon3 (1).png>)

* 시계방향(CW)으로 좌표 구성 : 외부로 판별되며 폴리곤의 외곽을 구성합니다.
* 반시계방향(CCW)으로 좌표 구성 : 내부로 판별되며 폴리곤의 홀(Hole)을 구성합니다.

하나의 폐곡선은 하나의 파트로 지정하며, 위 코드의 폴리곤은 점 수가 4개인 한 파트 구성됩니다.

만약 파트 수가 두 개(두 개의 홀과 하나의 외곽)인 폴리곤인 경우는 아래와 같이 구성됩니다.

```javascript
var vertex = new Module.JSVec3Array();
var part = new Module.Collection();

// Outside Circle
vertex.push(128.674986, 35.217478);
vertex.push(128.676652, 35.216556);
vertex.push(128.67549, 35.215182);
vertex.push(128.673796, 35.216007);
part.add(4);

// Inside Circle (Hole)
vertex.push(128.67637, 35.216512);
vertex.push(128.675038, 35.217213);
vertex.push(128.675953, 35.216049);
part.add(3);

// Inside Circle (Hole)
vertex.push(128.674922, 35.217041);
vertex.push(128.674217, 35.216088);
vertex.push(128.675412, 35.215423);
vertex.push(128.675856, 35.215953);
part.add(4);
```

지정한 좌표와 파트를 [setPartCoordinates](../object/jspolygon.md#setpartcoordinates-coordinates-parts-boolean) API로 설정합니다.

{% hint style="info" %}
각 파트의 순서는 자유롭게 설정해 주어도 되나, 적어도 파트 중 하나는 폴리곤의 외곽을 형성할 수 있도록 시계 방향(CW)으로 구성되어 있어야 합니다.
{% endhint %}

### step 3. 폴리곤 속성 지정 (선택)

폴리곤 좌표 외 폴리곤의 색상을 지정할 수 있습니다.

폴리곤은 기본 색상은 투명도가 0%인 흰색으로, 별도 색상을 지정하지 않는 경우 기본 색상이 설정됩니다.

폴리곤의 외곽 라인과 내부 채움 색상을 선택적으로 지정할 수 있습니다.

```javascript
var polygonStyle = new Module.JSPolygonStyle();

// 폴리곤 채움 색상
polygonStyle.setFill(true);
polygonStyle.setFillColor(new Module.JSColor(255, 0, 0));

// 폴리곤 외곽 색상
polygonStyle.setOutLine(true);
polygonStyle.setOutLineWidth(2.0);
polygonStyle.setOutLineColor(new Module.JSColor(0, 0, 255));

polygon.setStyle(polygonStyle);
```

### step 4. 레이어에 폴리곤 저장

레이어를 생성한 후 폴리곤 오브젝트를 추가합니다.

```javascript
var layerList = new Module.JSLayerList(true);
var layer = layerList.createLayer("POLYGON_LAYER", Module.ELT_POLYHEDRON);
layer.addObject(polygon, 0);
```

## 폴리곤 생성 결과

위 과정을 거쳐 여러 폴리곤을 한 레이어에 추가하면 아래와 같이 출력할 수 있습니다.

![](../.gitbook/assets/polygon4.png)

폴리곤 생성 과정에 대한 라이브 코드를 확인해 보고 싶으시다면? [여기](http://sandbox.dtwincloud.com/code/main.do?id=object\_polygon\_color)를 클릭해 주세요

높이를 지정한 폴리곤에 대한 라이브 코드를 확인해 보고 싶으시다면? [여기](http://sandbox.dtwincloud.com/code/main.do?id=object\_polygon\_height)를 클릭해 주세요
