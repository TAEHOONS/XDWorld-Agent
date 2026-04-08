---
description: 지도 내 박스(육면체) 형태의 공강 위치를 사용하기 위한 API 입니다.
---

# JSAABBox3D

> Module.JSAABBox3D() API를 생성합니다.
>
> JSAABBox3D 생성 시 기본값 min, max(JSVector3D(0.0, 0.0, 0.0), JSVector3D(0.0, 0.0, 0.0)) 설정으로 설정 됩니다.

```javascript
let min = new Module.JSVector3D(129.14, 35.18, 100.0);
let max = new Module.JSVector3D(129.18, 35.189, 200.0);
let boxDefault = new Module.JSAABBox3D(); // Both min and max are JSVector3D(0.0, 0.0, 0.0)
let boxWithMinMax = new Module.JSAABBox3D(min, max);
```

## properties

| Name | Type                                | Description     |
| :--- | :---------------------------------- | :-------------- |
| min  | [JSVector3D](../core/jsvector3d.md) | 최소 좌표 위치. |
| max  | [JSVector3D](../core/jsvector3d.md) | 최대 좌표 위치. |

### getBox() → [JSVec3Array](../core/jsvec3array.md)

> ECEF 좌표계에서의 AABB의 좌표를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   ECEF 좌표계에서의 AABB의 좌표를 경위도 좌표계로 반환합니다.

-   Return
    -   길이가 8인 [JSVec3Array](../core/jsvec3array.md)를 반환합니다.
    -   밑면 좌표 4개 + 윗면 좌표 4개

-   Sample  
    -   [Sandbox_View Mode](https://sandbox.egiscloud.com/code/main.do?id=object_aabb)

{% endtab %}
{% tab title="Template" %}

```javascript
var box = polygon.getBoundary();
// AABB Coordinates to Spherical Coordinates
// bottom(4), top(4)
var boxArray = box.getBox();

const corners = {
	bottom: [
		[boxArray.get(0).longitude, boxArray.get(0).latitude, boxArray.get(0).altitude],
		[boxArray.get(1).longitude, boxArray.get(1).latitude, boxArray.get(1).altitude],
		[boxArray.get(2).longitude, boxArray.get(2).latitude, boxArray.get(2).altitude],
		[boxArray.get(3).longitude, boxArray.get(3).latitude, boxArray.get(3).altitude],
	],
	top: [
		[boxArray.get(4).longitude, boxArray.get(4).latitude, boxArray.get(4).altitude],
		[boxArray.get(5).longitude, boxArray.get(5).latitude, boxArray.get(5).altitude],
		[boxArray.get(6).longitude, boxArray.get(6).latitude, boxArray.get(6).altitude],
		[boxArray.get(7).longitude, boxArray.get(7).latitude, boxArray.get(7).altitude],
	]
};
```

{% endtab %}
{% endtabs %}
