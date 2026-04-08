---
description: 지도 내 물 흐름 효과 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSFlowPolygon

> Module.createFlowPolygon API 생성.

```javascript
let flowPolygon = Module.createFlowPolygon("ID");
```

## Properties

| Name            | Type                                  | Description                                                                                                                                                  |
| --------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| opacity         | number                                | 투명도.                                                                                                                                                      |
| fluid_activity  | number                                | 물 흐름 시 출렁임 정도.                                                                                                                                      |
| flow_speed      | number                                | 흐름 속도.                                                                                                                                                   |
| image_type      | number                                | <p>이미지 표현 타입.<br>0: 지정 이미지 표현.<br>1: 물 흐름 방향 범례를 색상으로 표현.<br>3: 지형 텍스쳐와 물 흐름으로 표현.<br>그외: color 색상으로 표현.<p> |
| position_offset | [JSVector3D](../core/jsvector3d.md)   | 위치 추가 offset.                                                                                                                                            |
| color           | [JSColor](../core/jscolor.md)         | 범례 색상 표시 모드일 경우, 색상 설정.                                                                                                                       |
| coordinates     | [JSVec3Array](../core/jsvec3array.md) | 객체의 위치 좌표(경도, 위도, 고도).                                                                                                                          |

## Function

### createGrid(options) → object

> 격자 객체 생성

{% tabs %}
{% tab title="Information" %}

| Name    | Type                                                                          | Description         |
| ------- | ----------------------------------------------------------------------------- | ------------------- |
| options | [JSFlowPolygon.GridDataOption](jsflowpolygon.md#jsflowpolygon.griddataoption) | 그리드 정보 설정값. |

-   Return
    -   "result" 속성이 추가된 object : 객체 생성 성공.
    -   "error" 속성이 추가된 object : 객체 생성 실패.
        -   options에 "vertex" 속성이 없을 경우.
        -   options에 "index" 속성이 없을 경우.
        -   options에 "normaltexture" 속성이 없거나 해당 텍스처 이미지가 유효하지 않을 경우.
        -   그리드 객체 생성에 실패했을 경우.
        -   "waterlevel" 속성 설정에 실패했을 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### createWall(options) → object

> 수직 벽 객체 생성.

{% tabs %}
{% tab title="Information" %}

| Name    | Type                                                                          | Description        |
| ------- | ----------------------------------------------------------------------------- | ------------------ |
| options | [JSFlowPolygon.WallDataOption](jsflowpolygon.md#jsflowpolygon.walldataoption) | 수직 벽 생성 정보. |

-   Return
    -   "result" 속성이 추가된 object : 객체 생성 성공.
    -   "error" 속성이 추가된 object : 객체 생성 실패.
        -   options에 "vertex" 속성이 없을 경우.
        -   options에 "normaltexture" 속성이 없거나 해당 텍스처 이미지가 유효하지 않을 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setCullMode(type) → boolean

> 수직 벽면 폴리곤 컬링 옵션 설정.
>
> type 입력 값에 따른 컬링 옵션은 0(양면), 1(양면), 2(CW) 3(CCW).
>
> 컬링 옵션 초기 설정 3.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| type | number | 컬링모드.   |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
polygon.setCullMode(3);
```

{% endtab %}
{% endtabs %}

### create(options) → object

> 물 흐름 폴리곤 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type                                                                        | Description         |
| ------- | --------------------------------------------------------------------------- | ------------------- |
| options | [JSFlowPolygon.GridDataOption](#jsflowpolygongriddataoption)               | 폴리곤 생성 정보.   |

- Return  
  - `"result"` 속성이 포함된 object: 객체 생성 성공.  
  - `"error"` 속성이 포함된 object: 객체 생성 실패.  
    - `vertex` 또는 `normaltexture` 속성이 없을 경우.  
    - `normaltexture`, `flowtexture`, `flowpath`가 유효하지 않거나 없는 경우.  
    - 객체 생성 실패 또는 waterlevel 설정 실패 시.

{% endtab %}

{% tab title="Template" %}
```javascript
let flowPolygon = Module.createFlowPolygon("FLOW");

let normalIcon = new Module.JSIcon();
normalIcon.setPath("./data/normal_texture.png");

let flowIcon = new Module.JSIcon();
flowIcon.setPath("./data/flow_map.png");

let vertices = new Module.JSVec3Array();
vertices.push(new Module.JSVector3D(129.1, 35.1, 0));
vertices.push(new Module.JSVector3D(129.2, 35.1, 0));
vertices.push(new Module.JSVector3D(129.2, 35.2, 0));
vertices.push(new Module.JSVector3D(129.1, 35.2, 0));

let options = {
    vertex: vertices,
    normaltexture: normalIcon,
    flowtexture: flowIcon,
    waterlevel: 5.0
};

let result = flowPolygon.create(options);
```
{% endtab %}
{% endtabs %}


### Type Definitions

#### JSFlowPolygon.GridDataOption

> 격자 구성 정보.

| Name           | Type                                                                          | Attributes | Default         | Description                                       |
| -------------- | ----------------------------------------------------------------------------- | ---------- | --------------- | ------------------------------------------------- |
| vertex         | array([JSVector3D](../core/jsvector3d.md))                                    |            |                 | 격자를 구성하는 정점 좌표(경도, 위도, 고도) 목록. |
| index          | array(number)                                                                 |            |                 | 격자를 구성하는 정점에 대한 인덱스 목록.          |
| normaltexture  | [JSIcon](./jsicon.md)                                                         |            |                 | 재질 노말 텍스쳐.                                 |
| flowtexture    | [JSIcon](./jsicon.md)                                                         | optional   |                 | flow map(텍스처 직접 전달) .                      |
| flowpath       | array([JSVector2D](../core/jsvector2d.md))                                    | optional   |                 | flow map(path 전달).                              |
| imagetexture   | [JSIcon](./jsicon.md)                                                         | optional   |                 | 표면 이미지 텍스처.                               |
| waterlevel     | number                                                                        | optional   | 0.0             | 수위.                                             |
| positionoffset | [JSFlowPolygon.positionOffset](jsflowpolygon.md#jsflowpolygon.positionoffset) | optional   | (0.0, 0.0, 0.0) | 위치 offset.                                      |

#### JSFlowPolygon.WallDataOption

> 수직 벽 구성 정보.

| Name           | Type                                                                          | Attributes | Default         | Description                                         |
| -------------- | ----------------------------------------------------------------------------- | ---------- | --------------- | --------------------------------------------------- |
| vertex         | array([JSVector3D](../core/jsvector3d.md))                                    |            |                 | 수직벽을 구성하는 정점 좌표(경도, 위도, 고도) 목록. |
| normaltexture  | [JSIcon](./jsicon.md)                                                         |            |                 | 재질 노말 텍스처.                                   |
| imagetexture   | [JSIcon](./jsicon.md)                                                         | optional   |                 | 표면 이미지 텍스처.                                 |
| height         | number                                                                        | optional   | 10.0            | 벽 높이.                                            |
| positionoffset | [JSFlowPolygon.positionOffset](jsflowpolygon.md#jsflowpolygon.positionoffset) | optional   | (0.0, 0.0, 0.0) | 위치 offset.                                        |

#### JSFlowPolygon.positionOffset

| Name      | Type   | Default | Description |
| --------- | ------ | ------- | ----------- |
| longitude | number | 0.0     | 경도.       |
| latitude  | number | 0.0     | 위도.       |
| altitude  | number | 0.0     | 고도.       |
