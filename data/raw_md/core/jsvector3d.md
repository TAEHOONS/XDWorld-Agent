---
description: 지도 내 3차원 좌표와 관련된 기능을 관리하기 위한 API 입니다.
---

# JSVector3D

> Module.JSVector3D() API를 생성합니다.
>
> JSVector3D 생성 시 기본값 Longitude, Latitude, Altitude(0, 0, 0) 설정.

```javascript
var position = new Module.JSVector3D(129.128265, 35.171834, 100.0);

var position = new Module.JSVector3D();
```

## properties

| Name      | Type   | Description              |
| :-------- | :----- | :----------------------- |
| Longitude | number | 좌표 경도 (degrees 단위) |
| Latitude  | number | 좌표 위도 (degrees 단위) |
| Altitude  | number | 좌표 고도 (meter 단위)   |

## Function

### getDistance(position) → number

> 입력 변수값(position) 사이의 거리를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description  |
| :------- | :---------------------------------- | :----------- |
| position | [JSVector3D](../core/jsvector3d.md) | 비교할 좌표 |

-   Return
    -   number: 두 좌표 사이의 거리

{% endtab %}
{% tab title="Template" %}

```javascript
var position = new Module.JSVector3D(129.128265, 35.171834, 100.0);
var distance = position.getDistance(new Module.JSVector3D(129.138265, 35.161834, 100.0));
```

{% endtab %}
{% endtabs %}