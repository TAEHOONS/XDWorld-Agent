---
description: 지도 내 3차원 좌표 배열과 관련된 기능을 관리하기 위한 API 입니다.
---

# JSVec3Array

> Module.JSVec3Array() API를 생성합니다

```javascript
var vec_array = new Module.JSVec3Array();
```

## Function

### clear()

> 등록된 벡터 목록을 삭제합니다

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
vectorList.clear();
```

{% endtab %}
{% endtabs %}

### count() → number

> 등록된 벡터 개수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 등록 된 총 벡터 개수.

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
// ...
vectorList.count();
```

{% endtab %}
{% endtabs %}

### get(index) → [JSVector3D](../core/jsvector3d.md)

> 등록된 벡터 정보를 반환합니다.
>
> 입력 변수값(index) 인덱스에 해당하는 값을 반한합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description   |
| :---- | :----- | :------------ |
| index | number | 벡터 인덱스.. |

-   Return
    -   [JSVector3D](../core/jsvector3d.md)): 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
var vector = vectorList.get(2);
```

{% endtab %}
{% endtabs %}

### pop() → [JSVector3D](./jsvector3d.md)

> 벡터 목록 중 마지막 데이터를 반환합니다.
>
> 반환 후 마지막 벡터는 벡터 목록에서 삭제 됩니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
//...
var lastVector = vectorList.pop();
```

{% endtab %}
{% endtabs %}

### push(element) → number

> 새로운 벡터를 추가한다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type                                | Description      |
| :------ | :---------------------------------- | :--------------- |
| element | [JSVector3D](../core/jsvector3d.md) | 3차원 벡터 등록. |

-   Return
    -   number: 등록된 벡터 개수 반환.

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
var newVector = new Module.JSVector3d(100.0, 150.0);
vectorList.push(newVector);
```

{% endtab %}
{% endtabs %}

### pushLonLatAlt(lon, lat, alt) → number

> 입력 변수값(lon, lat, alt)으로 새로운 벡터 객체를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description               |
| :--- | :----- | :------------------------ |
| lon  | number | 좌표 경도 (degrees 단위). |
| lat  | number | 좌표 위도 (degrees 단위). |
| alt  | number | 좌표 고도 (meter 단위).   |

-   Return
    -   number: 등록된 벡터 개수 반환.

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
vectorList.pushLonLatAlt(100.0, 120.0, 15.0);
```

{% endtab %}
{% endtabs %}

### set(index, vec)

> 등록 벡터 데이터를 재 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description     |
| :---- | :---------------------------- | :-------------- |
| index | number                        | 인덱스 번호.    |
| vec   | [JSVector3D](./jsvector3d.md) | 재설정 벡터 값. |

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
//...
var newVector = new Module.JSVector3D(130.22, 149.3, 15.0);
vectorList.set(5, newVector);
```

{% endtab %}
{% endtabs %}

### setLonLatAlt(index, lon, lat, alt)

> 입력 변수값(index, lon, lat, alt)으로 벡터 객체를 수정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description               |
| :---- | :----- | :------------------------ |
| index | number | 인덱스 번호.              |
| lon   | number | 좌표 경도 (degrees 단위). |
| lat   | number | 좌표 위도 (degrees 단위). |
| alt   | number | 좌표 고도 (meter 단위).   |

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
//...
vectorList.setLonLatAlt(5, 130.22, 149.3, 15.0);
```

{% endtab %}
{% endtabs %}

### shift()

> 벡터 목록의 첫번쨰 벡터를 반환하고 두번째 벡터 목록의 첫번쨰 위치로 한칸씩 앞으로 이동한다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 반환성공.

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
//...
var lastVector = vectorList.shift();
```

{% endtab %}
{% endtabs %}

### removeDuplicateVectors(distance) → number

> 중복된 점을 제거합니다.
>
> 입력 변수값(distance) 보다 거리가 짧은 점들은 중복되는 것으로 간주하여 제거합니다.
>
> 제거된 점의 개수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description       |
| :------- | :----- | :---------------- |
| distance | number | 중복점 거리 기준 값. |

-   Return
    -   number: 제거된 점의 개수.

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec3Array();
//...
var removedCount = vectorList.removeDuplicateVectors(0.1);
```

{% endtab %}
{% endtabs %}

### getBoundary() → object

> 입력된 좌표리스트의 Boundary를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   min: [JSVector3D](../core/jsvector3d.md)
    -   max: [JSVector3D](../core/jsvector3d.md)

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### toJSVec2Array() → [JSVec2Array](../core/jsvec2array.md)

> 입력된 좌표리스트의 jsvec2array를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVec2Array](../core/jsvec2array.md): 반환성공.

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}