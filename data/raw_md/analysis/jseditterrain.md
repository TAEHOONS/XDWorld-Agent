---
description: 지도 내 지형 편집 기능 설정을 위한 API입니다.
---

# JSEditTerrain

> Module.getEditTerrain API를 생성합니다..

```javascript
var editTerrain = Module.getEditTerrain();
```

## Function

### clear() → boolean

> 지형 편집을 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

-   Sample
    -   function clearEditTerrain 참조.
    -   [Sandbox_Terrain Cut and Fill](https://sandbox.egiscloud.com/code/main.do?id=analysis_terrain_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### create(coordinates, height, angle) → boolean

> 지형 성절토를 수행합니다.
>
> 분석영역을 기준으로 수행합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                                   |
| :---------- | :------------------------------------ | :-------------------------------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 분석영역 좌표 목록 (경도, 위도, 고도).        |
| height      | number                                | 해발 고도 기준 성절토 기준 높이 (meter 단위). |
| angle       | number                                | 성절토 사면 각도 (degree 단위).               |

-   Sample
    -   function createEditTerrain 참조.
    -   [Sandbox_Terrain Cut and Fill](https://sandbox.egiscloud.com/code/main.do?id=analysis_terrain_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### createBoundary(min, max, height, angle) → boolean

> 지형 성절토를 수행합니다.
>
> 최소 좌표점, 최대 좌표점으로 구성된 경계박스 영역을 기준으로 수행합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                | Description                                   |
| :----- | :---------------------------------- | :-------------------------------------------- |
| min    | [JSVector2D](../core/jsvector2d.md) | 최소 좌표점 (경도, 위도).                     |
| max    | [JSVector2D](../core/jsvector2d.md) | 최대 좌표점 (경도, 위도).                     |
| height | number                              | 해발 고도 기준 성절토 기준 높이 (meter 단위). |
| angle  | number                              | 성절토 사면 각도 (degree 단위).               |

-   Sample
    -   function createEditTerrain 참조.
    -   [Sandbox_Terrain Cut and Fill](https://sandbox.egiscloud.com/code/main.do?id=analysis_terrain_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setEditFaceColor(data, width, height, type) → boolean

> 성절토 시 측명에 존재하는 사면에 이미지를 적용합니다.
>
> data 변수는 Uint8Array 기반의 바이너리 배열 데이터.

{% tabs %}
{% tab title="Information" %}

| Name   | Type    | Description                                              |
| :----- | :------ | :------------------------------------------------------- |
| data   | object  | 사면에 적용할 이미지 데이터.                             |
| width  | number  | 이미지 너비.                                             |
| height | number  | 이미지 높이.                                             |
| type   | boolean | <p>바닥면, 사면 구분<br>true: 바닥면<br>false: 사면 </p> |

-   Sample
    -   function createEditTerrain 참조.
    -   [Sandbox_Terrain Cut and Fill](https://sandbox.egiscloud.com/code/main.do?id=analysis_terrain_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}
