---
description: 지도 내 인덱스 맵을 설정 및 제어하기 위한 API 입니다.
---

# JSIndexMap3D

> Module.getIndexMap() API를 생성합니다.

```javascript
var map = Module.getIndexMap();
```

## Function

### setCameraTilt(tilt)

> 인덱스 맵에서 사용할 카메라 옵션을 설정합니다.
>
> 카메라 기울기(degrees 단위)를 변경합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description    |
| ---- | ------ | -------------- |
| tilt | number | 카메라 기울기. |

{% endtab %}

{% tab title="Template" %}

```javascript
var indexMap3D = Module.getIndexMap();
indexMap3D.setCameraTilt(89.9);
indexMap3D.setVisible(true);
```

{% endtab %}
{% endtabs %}

### setDistanceMinMax(min, max)

> 인덱스 맵에서 사용할 카메라 옵션을 설정합니다.
>
> 인덱스 맵과 카메라의 시야 최소, 최대 거리를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                     |
| ---- | ------ | ------------------------------- |
| min  | number | 가시화 최소 거리 (meters 단위). |
| max  | number | 가시화 최대 거리 (meters 단위). |

{% endtab %}

{% tab title="Template" %}

```javascript
var indexMap3D = Module.getIndexMap();
indexMap3D.setDistanceMinMax(50, 3000);
indexMap3D.setVisible(true);
```

{% endtab %}
{% endtabs %}

### setPosition(x, y)

> 인덱스 맵 위치를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                  |
| ---- | ------ | ---------------------------- |
| x    | number | 화면 X축 좌표 (pixels 단위). |
| y    | number | 화면 Y축 좌표 (pixels 단위). |

{% endtab %}

{% tab title="Template" %}

```javascript
var indexMap3D = Module.getIndexMap();
indexMap3D.setPosition(1300, 10);
indexMap3D.setVisible(true);
```

{% endtab %}
{% endtabs %}

### setSize(width, height)

> 인덱스 맵 가로 세로 크기 설정.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description              |
| ------ | ------ | ------------------------ |
| width  | number | 가로 크기 (pixels 단위). |
| height | number | 세로 크기 (pixels 단위). |

{% endtab %}

{% tab title="Template" %}

```javascript
var indexMap3D = Module.getIndexMap();
indexMap3D.setSize(400, 200);
indexMap3D.setVisible(true);
```

{% endtab %}
{% endtabs %}

### setVisible(visible)

> 인덱스 맵 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                                                 |
| ------- | ------- | ----------------------------------------------------------- |
| visible | boolean | <p>true: 인덱스 맵 가시화.<br>false: 인덱스 맵 비가시화.<p> |

{% endtab %}

{% tab title="Template" %}

```javascript
var indexMap3D = Module.getIndexMap();
indexMap3D.setVisible(true);
```

{% endtab %}
{% endtabs %}
